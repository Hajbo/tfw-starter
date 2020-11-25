import Image from "next/image";
import styles from "./styles.module.css";

const Header = () => (
  <div className={styles.header}>
    <div className={styles["logo-container"]}>
      <img alt="Avatao logo" src="/avatao_logo_dark.png" /> StartR
    </div>
  </div>
);

export default Header;
