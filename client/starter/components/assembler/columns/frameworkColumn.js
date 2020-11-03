import React from "react"
import styles from './styles.module.css'


class FrameworkColumn extends React.Component {

    constructor(props) {
        super(props);
        this.handleSelect = this.handleSelect.bind(this);
    }

    handleSelect(event) {
        this.props.onFrameworkSelect(event.target.value);
    }

    render() {
        return (
            <div className={styles['picker-column']}>
                {this.props.children ? this.props.children.map(framework => <div> <input type="radio" value={framework} name={this.props.name} onClick={this.handleSelect}/> {framework} </div>) : 'Please select a language'}  
            </div>
        )
    }
}


export default FrameworkColumn;