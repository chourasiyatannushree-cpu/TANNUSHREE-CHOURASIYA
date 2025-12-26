import "./App.css";
import { useForm } from "react-hook-form";

function App() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = (data) => {
    console.log(data);
    alert("Form Submitted Successfully");
  };

  return (
    <div className="container">
      <h2>React Hook Form</h2>

      <form onSubmit={handleSubmit(onSubmit)}>
        {/* First Name */}
        <div>
          <label>First Name:</label>
          <input
            {...register("firstName", { required: "First name is required" })}
          />
          {errors.firstName && (
            <p className="error">{errors.firstName.message}</p>
          )}
        </div>

        {/* Middle Name */}
        <div>
          <label>Middle Name:</label>
          <input {...register("middleName")} />
        </div>

        {/* Last Name */}
        <div>
          <label>Last Name:</label>
          <input
            {...register("lastName", { required: "Last name is required" })}
          />
          {errors.lastName && (
            <p className="error">{errors.lastName.message}</p>
          )}
        </div>

        {/* Email */}
        <div>
          <label>Email:</label>
          <input
            {...register("email", {
              required: "Email is required",
              pattern: {
                value: /^\S+@\S+$/i,
                message: "Invalid email",
              },
            })}
          />
          {errors.email && (
            <p className="error">{errors.email.message}</p>
          )}
        </div>

        {/* Password */}
        <div>
          <label>Password:</label>
          <input
            type="password"
            {...register("password", {
              required: "Password required",
              minLength: {
                value: 6,
                message: "Minimum 6 characters",
              },
            })}
          />
          {errors.password && (
            <p className="error">{errors.password.message}</p>
          )}
        </div>

        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default App;
