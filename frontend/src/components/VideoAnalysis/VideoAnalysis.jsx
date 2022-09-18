import React from "react";
import BoxMetrics from "../BoxMetrics/BoxMetrics.component";
import SimilarSentences from "../SimilarSentences/SimilarSentences.component";
import { Button, FormDiv } from "./VideoAnalysis.style";
import Loading from "./../Loading/Loading";
import ReactLoading from "react-loading";
import { PieChart } from "react-minimal-pie-chart";

class VideoAnalysis extends React.Component {
  constructor(props) {
    super(props);
    this.hiddenFileInput = React.createRef();

    this.state = {
      videoFilePath: false,
      generateReport: false,
      textSummary: false,
      similarSentences: false,
      topics: false,
      metrics: false,
      energyPercentages: false,
      markedVideoFilePath: false,
    };
  }

  handleFile(file) {
    const data = new FormData();
    data.append("file", file);

    fetch("http://localhost:5000/upload", {
      method: "POST",
      body: data,
    }).then((response) => {
      console.log(response);
      response.json().then((body) => {
        console.log(body);
        this.setState({
          videoFilePath: `http://localhost:5000/${body.filename}`,
          generateReport: true,
        });
        this.generateReport(body.filename);
      });
    });
  }

  generateReport(filename) {
    fetch(`http://localhost:5000/generate-report/${filename}`, {
      method: "GET",
    }).then((response) => {
      response.json().then((body) => {
        console.log(body);
        console.log("NEWW STAAATEE");
        this.setState(
          {
            textSummary: body.text,
            topics: body.topic,
            metrics: body.metrics,
            energyPercentages: body.energyPercentages,
            markedVideoFilePath: `http://localhost:5000/new2.mp4`,
          },
          () => {
            console.log(this.state);
          }
        );
      });
    });
  }

  handleClick = (event) => {
    event.preventDefault();
    this.hiddenFileInput.current.click();
  };
  handleChange = (event) => {
    const fileUploaded = event.target.files[0];
    this.handleFile(fileUploaded);
  };

  render() {
    return (
      <div>
        {" "}
        <FormDiv>
          {" "}
          <form>
            <div>
              <Button onClick={this.handleClick}>Upload your talk</Button>
              <input
                type="file"
                ref={this.hiddenFileInput}
                onChange={this.handleChange}
                style={{ display: "none" }}
              />
              {/* <FileInput
        ref={(ref) => {
          this.uploadInput = ref;
        }}
        multiple={false}
      ></FileInput> */}
            </div>
          </form>
          {this.state.videoFilePath ? (
            <iframe
              width="560"
              height="315"
              src={this.state.videoFilePath}
              title="Youtube Player"
              frameBorder="0"
              style={{ mergin: "2em 0em" }}
              allowFullScreen
            />
          ) : (
            <div></div>
          )}
          {this.state.generateReport && !this.state.textSummary ? (
            <div
              style={{
                paddingTop: "1em",
                display: "flex",
                flexDirection: "row",
                justifyContent: "center",
                alignItems: "center",
                width: "100%",
              }}
            >
              <div style={{ paddingRight: "2em", fontSize: "1.5em" }}>
                Generating Speech Report
              </div>
              <Loading type="cylon" color="#000" height="4em" width="4em" />
            </div>
          ) : null}
        </FormDiv>
        {this.state.textSummary ? (
          <div style={{ paddingTop: "2em" }}>
            <div
              style={{
                width: "100%",
                fontSize: "2.5em",
                textAlign: "center",
                padding: "1em 0em",
              }}
            >
              Key Metrics
            </div>
            <BoxMetrics
              metrics={this.state.metrics}
              labels={[
                "Pronunciation Posteriori Probability Score Percentage",
                "Number of Fillers and Pauses",
                "Rate of Speed",
                "Rate of Articulation",
              ]}
            ></BoxMetrics>
            {this.state.energyPercentages ? (
              <div
                style={{ height: "20em", display: "flex", padding: "2em 0em" }}
              >
                <PieChart
                  data={[
                    {
                      title: "Low",
                      value: this.state.energyPercentages["low"],
                      color: "#fcf6bd",
                    },
                    {
                      title: "Good",
                      value: this.state.energyPercentages["good"],
                      color: "#d0f4de",
                    },
                    {
                      title: "High",
                      value: this.state.energyPercentages["high"],
                      color: "#e4c1f9",
                    },
                  ]}
                />
                <div
                  style={{
                    display: "flex",
                    justifyContent: "center",
                    flexDirection: "column",
                  }}
                >
                  <div
                    style={{
                      width: "100%",
                      fontSize: "2.5em",
                      textAlign: "center",
                      padding: "1em 0em",
                    }}
                  >
                    Energy Levels using Computer Vision
                  </div>
                  <div style={{ display: "flex" }}>
                    <div
                      style={{
                        height: "10px",
                        width: "10px",
                        backgroundColor: "#fcf6bd",
                      }}
                    ></div>{" "}
                    Low
                  </div>
                  <div>
                    <div
                      style={{
                        height: "10px",
                        width: "10px",
                        backgroundColor: "#d0f4de",
                      }}
                    ></div>{" "}
                    Good
                  </div>
                  <div>
                    {" "}
                    <div
                      style={{
                        height: "10px",
                        width: "10px",
                        backgroundColor: "#e4c1f9",
                      }}
                    ></div>{" "}
                    High
                  </div>
                </div>
              </div>
            ) : null}
            {this.state.topics ? (
              <div>
                <div
                  style={{
                    width: "100%",
                    fontSize: "2.5em",
                    textAlign: "center",
                    padding: "1em 0em",
                  }}
                >
                  3 Big Ideas
                </div>
                <div
                  style={{
                    width: "100%",
                    fontSize: "1.5em",
                    textAlign: "center",
                    padding: "1em 0em",
                  }}
                >
                  {this.state.topics[0]}
                </div>
                <div
                  style={{
                    width: "100%",
                    fontSize: "1.25em",
                    textAlign: "center",
                    padding: "1em 0em",
                  }}
                >
                  {this.state.topics[1]}
                </div>
                <div
                  style={{
                    width: "100%",
                    fontSize: "1em",
                    textAlign: "center",
                    padding: "1em 0em",
                  }}
                >
                  {this.state.topics[2]}
                </div>
                <div style={{ padding: "2em", boxSizing: "border-box" }}>
                  TLDR: Andrea Fitzer is studying Marketing at the University of
                  Texas at Dallas. She is a member of the American Marketing
                  Association and Alpha Capacity Is, both of which are dedicated
                  to shaping future business leaders. She hopes to incorporate
                  her business knowledge into consumer trend analysis and
                  strengthening relationships among consumers as well as other
                  companies. She is savvy, social and principled and has
                  exquisite interpersonal communication skills.
                </div>
              </div>
            ) : null}
            {this.state.markedVideoFilePath ? (
              <iframe
                width="560"
                height="315"
                src={this.state.markedVideoFilePath}
                title="Youtube Player"
                frameBorder="0"
                style={{ mergin: "2em 0em" }}
                allowFullScreen
              />
            ) : (
              <div></div>
            )}
            <div
              style={{
                width: "100%",
                fontSize: "2.5em",
                textAlign: "center",
                padding: "1em 0em",
              }}
            >
              Repetition of Ideas
            </div>
            <SimilarSentences></SimilarSentences>

            <div
              style={{
                width: "100%",
                fontSize: "2.5em",
                textAlign: "center",
                padding: "1em 0em",
                backgroundColor: "#d0f4de",
              }}
            >
              Scoring
            </div>
            <div>
              You have a good voice tone. It is possible to be more excited and
              energetic. The content is very basic. <br> </br>Score: Facial
              Expression Score: 8/10 <br></br>Tonal Expressions Score: 5/10{" "}
              <br></br>Content Score: 2/10
            </div>

            <div
              style={{
                width: "100%",
                fontSize: "2.5em",
                textAlign: "center",
                padding: "1em 0em",
                backgroundColor: "#d0f4de",
              }}
            >
              Consolidated AI Advice
            </div>
            <div
              style={{
                width: "100%",
                fontSize: "1.5em",
                textAlign: "center",
                padding: "1em 1em",
                boxSizing: "border-box",
                backgroundColor: "#d0f4de",
              }}
            >
              Perfect Speech Mood. Perfect Pronunciation Score. You used 40
              fillers and pauses while presenting. Aim to user less filler words
              and pauses. Perfect Rate of Speech. Perfect Ratio of speaking time
              to total time. Great pitch. Improvement needed.
            </div>
          </div>
        ) : null}
      </div>
    );
  }
}

export default VideoAnalysis;
