import React from "react"
import {FrameworkColumn, LanguageColumn, AllModulesColumn, SelectedModulesColumn} from './columns'
import styles from './styles.module.css'


const test = [
    'A', 'B', 'C', 'D'
]

const selectedModules = [
    {'name': 'A'}
]

const allModules = [{'name': 'A'}, {'name': 'B'}, {'name': 'C'}, {'name': 'D'}]

class Assembler extends React.Component  {

    constructor(props) {
        super(props);
        this.state = {
            languages: {
                all: props.languages,
                selected: null
            },
            frameworks: {
                all: null,
                selected: null
            },
            modules: {
                all: null,
                selected: null
            }
        };

        this.handleLanguageSelect = this.handleLanguageSelect.bind(this);
        this.handleFrameworkSelect = this.handleFrameworkSelect.bind(this);
        this.handleAddModule = this.handleAddModule.bind(this);
        this.handleRemoveModule = this.handleRemoveModule.bind(this);
    };

    handleLanguageSelect(selectedLanguage) {
        fetch(`http://localhost:5000/api/v1/languages/${selectedLanguage}`)
            .then(res => res.json())
            .then(res => {
                this.setState({
                    languages: {
                        all: this.state.languages.all,
                        selected: selectedLanguage
                    },
                    frameworks: {
                        all: res.supported_frameworks, // Some magic fetch
                        selected: null
                    },
                    modules: this.state.modules
                })
            })
        }
        

    handleFrameworkSelect(selectedFramework) {
        fetch(`http://localhost:5000/api/v1/languages/${this.state.languages.selected}/${selectedFramework}`)
            .then(res => res.json())
            .then(res => {
                this.setState({
                    languages: this.state.languages,
                    frameworks: {
                        all: this.state.frameworks.all,
                        selected: selectedFramework
                    },
                    modules: {
                        all: res.modules.optional.filter(module => !res.modules.mandatory.map(m => m.name).includes(module.name) ), // Some magic fetch
                        selected: res.modules.mandatory // Some magic fetch
                    }
                })
            })
    }


    handleAddModule(toAdd) {
        console.log(toAdd);
        this.setState({
            languages: this.state.languages,
            frameworks: this.state.frameworks,
            modules: {
                all: this.state.modules.all.filter(existingModule => existingModule.name != toAdd.name),
                selected: this.state.modules.selected.concat(toAdd),
            }
        })
    }

    handleRemoveModule(toRemove) {
        this.setState({
            languages: this.state.languages,
            frameworks: this.state.frameworks,
            modules: {
                all: this.state.modules.all.concat([toRemove]),
                selected: this.state.modules.selected.filter(existingModule => existingModule.name != toRemove.name)
            }
        })
    }

    render() {
        return(
            <div className={styles.assembler}>
                <LanguageColumn 
                    children={this.state.languages.all} name='languages'
                    onLanguageSelect={this.handleLanguageSelect}
                />
                <FrameworkColumn 
                    children={this.state.frameworks.all} name='frameworks'
                    onFrameworkSelect={this.handleFrameworkSelect}
                />
                <SelectedModulesColumn 
                    children={this.state.modules.selected}
                    onRemoveModule={this.handleRemoveModule}
                />
                <AllModulesColumn 
                    children={this.state.modules.all}
                    onAddModule={this.handleAddModule}
                />
            </div>
        )
    }
}


export default Assembler;