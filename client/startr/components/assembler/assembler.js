import React from "react";
import {
  FrameworkColumn,
  LanguageColumn,
  AllModulesColumn,
  SelectedModulesColumn,
} from "./columns";
import { DownloadButton } from "./button";
import styles from "./styles.module.css";

class Assembler extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      languages: {
        all: props.languages,
        selected: null,
      },
      frameworks: {
        all: null,
        selected: null,
      },
      modules: {
        all: null,
        selected: null,
      },
    };

    this.handleLanguageSelect = this.handleLanguageSelect.bind(this);
    this.handleFrameworkSelect = this.handleFrameworkSelect.bind(this);
    this.handleAddModule = this.handleAddModule.bind(this);
    this.handleRemoveModule = this.handleRemoveModule.bind(this);
    this.addExtraDependency = this.addExtraDependency.bind(this);
  }

  handleLanguageSelect(selectedLanguage) {
    fetch(`http://localhost:5000/api/v1/languages/${selectedLanguage}`)
      .then((res) => res.json())
      .then((res) => {
        this.setState({
          languages: {
            all: this.state.languages.all,
            selected: selectedLanguage,
          },
          frameworks: {
            all: res.supported_frameworks,
            selected: null,
          },
          modules: {
            all: null,
            selected: null,
          },
        });
      });
  }

  handleFrameworkSelect(selectedFramework) {
    fetch(
      `http://localhost:5000/api/v1/languages/${this.state.languages.selected}/frameworks/${selectedFramework}`
    )
      .then((res) => res.json())
      .then((res) => {
        this.setState({
          languages: this.state.languages,
          frameworks: {
            all: this.state.frameworks.all,
            selected: selectedFramework,
          },
          modules: {
            all: res.modules.optional.filter(
              (module) =>
                !res.modules.mandatory.map((m) => m.name).includes(module.name)
            ),
            selected: res.modules.mandatory,
          },
        });
      });
  }

  handleAddModule(toAdd) {
    this.setState({
      languages: this.state.languages,
      frameworks: this.state.frameworks,
      modules: {
        all: this.state.modules.all.filter(
          (existingModule) => existingModule.name != toAdd.name
        ),
        selected: this.state.modules.selected.concat(toAdd),
      },
    });
  }

  handleRemoveModule(toRemove) {
    this.setState({
      languages: this.state.languages,
      frameworks: this.state.frameworks,
      modules: {
        all: this.state.modules.all.concat([toRemove]),
        selected: this.state.modules.selected.filter(
          (existingModule) => existingModule.name != toRemove.name
        ),
      },
    });
  }

  addExtraDependency(dependency) {
    this.setState({
      languages: this.state.languages,
      frameworks: this.state.frameworks,
      modules: {
        all: this.state.modules.all,
        selected: this.state.modules.selected.concat([dependency]),
      },
    });
  }

  render() {
    return (
      <div className={styles.main}>
        <div className={styles.assembler}>
          <LanguageColumn
            children={this.state.languages.all}
            name="languages"
            onLanguageSelect={this.handleLanguageSelect}
          />
          <FrameworkColumn
            children={this.state.frameworks.all}
            name="frameworks"
            onFrameworkSelect={this.handleFrameworkSelect}
          />
          <SelectedModulesColumn
            children={this.state.modules.selected}
            onRemoveModule={this.handleRemoveModule}
            addExtraDependency={this.addExtraDependency}
          />
          <AllModulesColumn
            children={this.state.modules.all}
            onAddModule={this.handleAddModule}
          />
        </div>

        <DownloadButton
          language={this.state.languages.selected}
          framework={this.state.frameworks.selected}
          modules={this.state.modules.selected}
        />
      </div>
    );
  }
}

export default Assembler;
