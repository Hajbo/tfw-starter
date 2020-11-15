import React from "react";
import {DependencyAddButton} from "../button";


class Modal extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            name: null,
            version: null
        }

        this.setName = this.setName.bind(this);
        this.setVersion = this.setVersion.bind(this);
        this.onSave = this.onSave.bind(this);
      }

    setName(name) {
        this.setState({
            name: name,
            version: this.state.version
        });
    }

    setVersion(version) {
        this.setState({
            name: this.state.name,
            version: version
        });
    }

    onSave() {
        this.props.onSave(this.state);
    }
    
  render() {
    if (!this.props.isOpen) {
      return null;
    };

    const BackgroundStyle = {
        backgroundColor: "rgba(220,220,220,0.5)",
        position: "fixed",
        top: 0,
        right: 0,
        bottom: 0,
        left: 0
      };
  
      const ModalStyle = {
        maxWidth: 500,
        minHeight: 230,
        backgroundColor: "#fff",
        margin: "5% auto",
        padding: 5
      };
  
      const HeaderStyle = {
        height: 20,
        width: "100%"
      };
  
      const CloseBtnStyle = {
        float: "right",
        cursor: "pointer",
        display: "block"
      };

      const ModalForm = {
        display: "flex",
        flexFlow: "column",
        padding: "15px",
      };

      const FlexRow = {
        display: "flex",
        width: "100%",
        justifyContent: "space-between",
        padding: "15px",
      };

      const WideInput = {
          width: "80%",
      }
  
      return (
        <div style={BackgroundStyle}>
          <div style={ModalStyle}>
            <div style={HeaderStyle}>
              <span style={CloseBtnStyle} onClick={this.props.onClose}>
              <i
                className="fa fa-times"
            ></i>
              </span>
              <div style={ModalForm}>
                <div style={FlexRow}>
                    <label htmlFor="dependencyName">Name</label>
                    <input style={WideInput} type="text" id="dependencyName" required onChange={(e) => this.setName(e.target.value)}/>
                </div>
                <div style={FlexRow}>
                    <label htmlFor="dependencyVersion">Version</label>
                    <input style={WideInput} type="text" id="dependencyVersion" required onChange={(e) => this.setVersion(e.target.value)}/>
                </div>
                <DependencyAddButton onClick={(e) => {this.onSave(); this.props.onClose();}} disabled={!(this.state.name && this.state.version)}/>
              </div>
            </div>
            {this.props.children}
          </div>
        </div>
      );
  };
};

export default Modal;
