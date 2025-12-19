import { useState } from "react";

const names = ["Tannu", "Aman", "Ravi", "Neha"];

const SearchFilter = () => {
  const [search, setSearch] = useState("");

  return (
    <div>
      <input
        placeholder="Search name"
        onChange={(e) => setSearch(e.target.value)}
      />
      <ul>
        {names
          .filter((n) => n.toLowerCase().includes(search.toLowerCase()))
          .map((n, i) => <li key={i}>{n}</li>)}
      </ul>
    </div>
  );
};

export default SearchFilter;
