import React from "react";

class FileUploadForm extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      videoFilePath: false,
      generateReport: false,
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
    this.generateReport = this.generateReport.bind(this);
  }

  handleUploadImage(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append("file", this.uploadInput.files[0]);

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
        console.log(body.text);
      });
    });
  }

  render() {
    return (
      <form onSubmit={this.handleUploadImage}>
        <div>
          <input
            ref={(ref) => {
              this.uploadInput = ref;
            }}
            type="file"
          />
        </div>
        <br />
        <div>
          <button>Upload</button>
        </div>

        {this.state.videoFilePath ? (
          <iframe
            width="560"
            height="315"
            src={this.state.videoFilePath}
            title="Youtube Player"
            frameborder="0"
            allowFullScreen
          />
        ) : (
          <div></div>
        )}
      </form>
    );
  }
}

export default FileUploadForm;
