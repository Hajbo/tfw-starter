import React from "react"
import styles from './styles.module.css'
import download from 'downloadjs'


class DownloadButton extends React.Component {

    constructor(props) {
        super(props);
        this.downloadStarter = this.downloadStarter.bind(this);
    }

    async downloadStarter() {
        var filenameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
        var data = {
            language: this.props.language,
            framework: this.props.framework,
            modules: this.props.modules
        }
        
        var resp = await fetch('http://localhost:5000/api/v1/assemble', {
            method: 'POST',
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })

        var blob = await resp.blob();
        var matches = filenameRegex.exec(resp.headers.get('content-disposition'));
        return download(blob, matches[1]);
    }

    render() {
        return (
            <button className={styles['download-button']} onClick={this.downloadStarter} disabled={! (this.props.language && this.props.framework && this.props.modules)}>
                Download
            </button>
        )
    }
}


export default DownloadButton;
