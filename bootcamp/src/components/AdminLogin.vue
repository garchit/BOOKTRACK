<template>
    <div class="container mt-5">
      <h1 class="mb-4">Admin's Login</h1>
      <form @submit.prevent="login">
        <div class="form-group">
          <label for="username">Enter Your Username:</label>
          <input type="text" class="form-control" v-model="username" required>
        </div>
        <div class="form-group">
          <label for="password">Enter Your Password:</label>
          <input type="password" class="form-control" v-model="password" required>
        </div>
        <button type="submit" class="btn btn-primary">Login</button>
      </form>
      <!-- Success alert -->
      <div v-if="successMessage" class="alert alert-success mt-3" role="alert">
        {{ successMessage }}
      </div>
      <!-- Error alert -->
      <div v-if="errorMessage" class="alert alert-danger mt-3" role="alert">
        {{ errorMessage }}
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
        successMessage: '',
        errorMessage: ''
      };
    },
    methods: {
      login() {
        // Handle form submission
        const formData = {
          username: this.username,
          password: this.password
        };
        this.$axios.post("/admin_login", formData)
          .then(() => {
            // Clear previous error message
            this.errorMessage = '';
            // Set success message
            // localStorage.setItem("access_token", access_token);
            localStorage.setItem('userRole', 'admin');
            this.successMessage = 'Login successful';
            // Redirect to admin dashboard
            setTimeout(() => {
            this.$router.push("/adminDashboard");
          }, 2000);
            // this.$router.push("/adminDashboard");
          })
          .catch((error) => {
            // Clear previous success message
            this.successMessage = '';
            // Handle error response
            if (error.response && error.response.data && error.response.data.message) {
              this.errorMessage = error.response.data.message;
            } else {
              console.error("An unknown error occurred:", error);
              this.errorMessage = "An unknown error occurred";
            }
          });
      }
    }
  };
  </script>
  
  <style scoped>
  /* Custom styles can go here */
  </style>
  