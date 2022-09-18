import React from "react";
import { Button, FormDiv } from "./FileUploadForm.style";

class FileUploadForm extends React.Component {
  constructor(props) {
    super(props);
    this.hiddenFileInput = React.createRef();

    this.state = {
      videoFilePath: false,
      generateReport: false,
      textSummary: false,
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
        this.setState({
          textSummary: body.text,
        });
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
            frameborder="0"
            style={{ mergin: "2em 0em" }}
            allowFullScreen
          />
        ) : (
          <div></div>
        )}
      </FormDiv>
    );
  }
}

export default FileUploadForm;
