import React from "react"
import classNames from "classnames"
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
            <div className={classNames(styles['language-column'], this.props.name)}>
                {this.props.children ? this.props.children.map(language => <div className={styles.row} key={classNames(language, 'item')}> 
                    <input type="radio" value={language} id={language} name={this.props.name} onClick={this.handleSelect}/> 
                    <label for={language}>{language}</label>
                    </div>) : 'Something went wrong 😨'}  
            </div>
        )
    }
}


export default LanguageColumn;