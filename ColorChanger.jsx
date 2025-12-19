import { useState } from "react";

const ColorChanger = () => {
  const [color, setColor] = useState("white");

  return (
    <div style={{ background: color, height: "150px" }}>
      <button onClick={() => setColor("red")}>Red</button>
      <button onClick={() => setColor("blue")}>Blue</button>
      <button onClick={() => setColor("green")}>Green</button>
    </div>
  );
};

export default ColorChanger;
