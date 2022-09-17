
import cohere
from dotenv import load_dotenv
import os
import numpy as np
from numpy.linalg import norm
from annoy import AnnoyIndex
import pandas as pd

def configure():
    load_dotenv()

# _text = "Generating random paragraphs can be an excellent way for writers to get their creative flow going at the beginning of the day. The writer has no idea what topic the random paragraph will be about when it appears. This forces the writer to use creativity to complete one of three common writing challenges. The writer can use the paragraph as the first one of a short story and build upon it. A second option is to use the random paragraph somewhere in a short story they create. The third option is to have the random paragraph be the ending paragraph in a short story. No matter which of these challenges is undertaken, the writer is forced to use creativity to incorporate the paragraph into their writing. A random paragraph can also be an excellent way for a writer to tackle writers' block. Writing block can often happen due to being stuck with a current project that the writer is trying to complete. By inserting a completely random paragraph from which to begin, it can take down some of the issues that may have been causing the writers' block in the first place. Another writing challenge can be to take the individual sentences in the random paragraph and incorporate a single sentence from that into a new paragraph to create a short story. Unlike the random sentence generator, the sentences from the random paragraph will have some connection to one another so it will be a bit different. You also won't know exactly how many sentences will appear in the random paragraph."

_text = "So in my last video, I talked about giving a selfintroduction presentation and I talked about the importance of relating who you are to your audience to make sure that they will be engaged with what you're talking about and really care about who you are as a person. In this video, I want to talk about what you can say specifically when you're giving a speech. I present what you can say when you're speaking. Introduction hi, my name is Karl Kwan. This channel here is all about learning presentation skills. I'll teach you how tos tips and tricks to give better presentations. You'll also see some of my work videos."

configure()

def splitText(text):
    textArray = text.split('.')
    df = pd.DataFrame([i for i in textArray if i!=""])
    print(df.head(10))
    return df

def getSimilarityMatrix(_text):
    df = splitText(_text)
    embeddings = embed(list(df[0]), os.getenv('api_key'))
    

    distances = []

    for n1 in range(len(embeddings)):
        temp = []
        for n2 in range(len(embeddings)):
            temp.append(cosineDistance(embeddings[n1], embeddings[n2]))
        
        distances.append(temp)
    
    print(distances)

def embed(df, key):

    co = cohere.Client(key)
    response = co.embed(texts=list(df[0]))

    embeds = response.embeddings
    # print('Embeddings: {}'.format(embeds))
    return embeds



def getSearchIndex(_text):
    df = splitText(_text)
    embeds = embed(df, os.getenv('api_key'))

    std = np.std(embeds)
    print(std)

    # Create the search index, pass the size of embedding
    search_index = AnnoyIndex(len(embeds[0]), 'angular')
    # Add all the vectors to the search index
    for i in range(len(embeds)):
        search_index.add_item(i, embeds[i])

    search_index.build(10) # 10 trees
    # search_index.save('lda_models/test.ann')

    return df, search_index


    

def searchSimilar(df, _size, search_index, window = 3, thres = 0.82):
    
    # for n1 in range(_size):
    #     similar_item_ids = search_index.get_nns_by_item(n1,10,
    #                                             include_distances=True)
    #     # Format and print the text and distances
    #     results = pd.DataFrame(data={'texts': df.iloc[similar_item_ids[0]][0],
    #                                 'distance': similar_item_ids[1]}).drop(n1)

    #     print("\n")
    #     print(f">>> Question:'{df.iloc[n1][0]}'\nNearest neighbors:")
    #     print(results)



    for n1 in range(_size-window):
        print("n1:")
        for n2 in range(n1+1, n1 + window):
            distance = search_index.get_distance(n1, n2)
            # print(distance)
            if distance < thres:
                print("\n >>> ", n1, n2, "These ideas might be repeating and are too close")
    

def test(_text):
    df, search_index = getSearchIndex(_text)
    searchSimilar(df, search_index.get_n_items(), search_index, 3)

test(_text)


    
