import { useState } from "react";

const ToggleText = () => {
  const [show, setShow] = useState(true);

  return (
    <div>
      <button onClick={() => setShow(!show)}>
        {show ? "Hide" : "Show"}
      </button>
      {show && <p>Hello React 👋</p>}
    </div>
  );
};

export default ToggleText;
