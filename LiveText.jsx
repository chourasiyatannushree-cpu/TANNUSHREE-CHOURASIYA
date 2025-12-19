import { useState } from "react";

const LiveText = () => {
  const [text, setText] = useState("");

  return (
    <div>
      <input
        type="text"
        placeholder="Type here"
        onChange={(e) => setText(e.target.value)}
      />
      <p>{text}</p>
      <button onClick={() => setText("")}>Clear</button>
    </div>
  );
};

export default LiveText;
