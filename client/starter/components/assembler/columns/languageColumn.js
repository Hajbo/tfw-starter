import React from "react"
import styles from './styles.module.css'


class LanguageColumn extends React.Component {

    constructor(props) {
        super(props);
        this.handleSelect = this.handleSelect.bind(this);
    }

    handleSelect(event) {
        this.props.onLanguageSelect(event.target.value);
    }

    render() {
        return (
            <div className={styles['picker-column']}>
                {this.props.children ? this.props.children.map(language => <div> <input type="radio" value={language} name={this.props.name} onClick={this.handleSelect}/> {language} </div>) : 'Something went wrong 😨'}  
            </div>
        )
    }
}


export default LanguageColumn;