import "./App.css";
import logoImage from "./assets/logo.png"; // Import the image
import checkImage from "./assets/check.png"; // Import the image

function App() {
  return (
    <>
      <div className="header">
        <div className="logo">
          <img src={logoImage} alt="" />
          <p>HYDRO-TRACK</p>
        </div>
        <div className="heading">
          <h1>DASHBOARD</h1>
        </div>
      </div>
      <div className="container">
        <div className="item map" />
        <div className="item water_flow">
          <div className="card">
            <p>WATER FLOW</p>
          </div>
        </div>
        <div className="item water_level">
          <div className="card">
            <p>WATER LEVEL</p>
          </div>
        </div>
        <div className="item status">
          <div className="card">
            <p>Motor and Valve Status</p>
          </div>
        </div>
        <div className="item usage" />
      </div>
      <div className="footer">
        <img src={checkImage} alt="" />
        <p>All Systems Operating Normally</p>
      </div>
    </>
  );
}

export default App;
