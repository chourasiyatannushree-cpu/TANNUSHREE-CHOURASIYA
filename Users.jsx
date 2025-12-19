import { useEffect, useState } from "react";

const Users = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then(res => res.json())
      .then(data => setUsers(data));
  }, []);

  return (
    <div>
      <h3>Users</h3>
      {users.map(user => (
        <p key={user.id}>{user.name} - {user.email}</p>
      ))}
    </div>
  );
};

export default Users;
