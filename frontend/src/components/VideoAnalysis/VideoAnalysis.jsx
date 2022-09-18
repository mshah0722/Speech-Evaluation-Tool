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
        console.log(body.text);
        console.log(body.topic);
        this.setState(
          {
            textSummary: body.text,
            topics: body.topic,
          },
          console.log(this.state)
        );
      });
    });
  }

  handleClick = (event) => {
    event.preventDefault();
    console.log("handle click");
    console.log(event);
    console.log(this.hiddenFileInput);
    this.hiddenFileInput.current.click();
  };
  handleChange = (event) => {
    console.log("in");
    const fileUploaded = event.target.files[0];
    console.log(fileUploaded);
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
        <div style={{ width: "30%", padding: "5em" }}></div>
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
            <BoxMetrics></BoxMetrics>
            <PieChart
              data={[
                { title: "One", value: 10, color: "#E38627" },
                { title: "Two", value: 15, color: "#C13C37" },
                { title: "Three", value: 20, color: "#6A2135" },
              ]}
            />
            ;
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
              </div>
            ) : null}
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
          </div>
        ) : null}
      </div>
    );
  }
}

export default VideoAnalysis;
