import Header from "./header";
import styles from "./styles.module.css";

const Layout = ({ children }) => (
  <div className={styles.main}>
    <Header />
    {children}
  </div>
);

export default Layout;
