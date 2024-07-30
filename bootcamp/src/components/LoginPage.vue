<!-- 
  <template>
    <div class="signup-container">
        <div class="signup-form">
            <h2>Sign Up</h2>
            <form @submit.prevent="signup">
                
                <label for="username">Username</label>
                <input type="text" v-model="username" required>
                
               
                <label for="password">Password</label>
                <input type="password" v-model="password" required>
               
                <button type="submit">Login</button>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
          
            username: "",
            password: "",           
        };
    },
    methods: {
        
        signup() {
           
         

            const formData = {
               
                username: this.username,
               
                password: this.password,
               
            };
            this.$axios
                .post("/login", formData)
                .then(() => {
                    this.$router.push("/dashboard");
                    
                })
                
                .catch((error) => {
    if (error.response && error.response.data && error.response.data.message) {
        console.error(error.response.data.message);
       
    } else {
        console.error("An unknown error occurred:", error);
        this.$toast.error("An unknown error occurred", {
            position: 'top-right',
            duration: 5000,
        });
    }
});

        },
    },
};
</script>
<style scoped>
.signup-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

.signup-form {
    text-align: center;
    background-color: #ffffff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    width: 320px;
}

h2 {
    margin-bottom: 16px;
    font-size: 24px;
}

label {
    font-size: 14px;
    font-weight: bold;
    display: block;
    margin-bottom: 6px;
}

input[type="text"],
input[type="password"],input[type="email"] {
    width: 80%;
    padding: 10px;
    margin-bottom: 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
}

button {
    background-color: #007bff;
    color: #ffffff;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    font-size: 14px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
</style>
   -->


<template>
  <div class="signup-container">
    <div class="signup-form">
      <h2>Sign Up</h2>
      <form @submit.prevent="signup">
        <label for="username">Username</label>
        <input type="text" v-model="username" required>

        <label for="password">Password</label>
        <input type="password" v-model="password" required>

        <button type="submit">Login</button>
      </form>
      <div v-if="successAlertVisible" class="alert alert-success" role="alert">
        Login successful! Redirecting to dashboard...
      </div>
      <div v-if="errorAlertVisible" class="alert alert-danger" role="alert">
        {{ errorMessage }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
      successAlertVisible: false,
      errorAlertVisible: false,
      errorMessage: ""
    };
  },
  methods: {
    signup() {
      const formData = {
        username: this.username,
        password: this.password,
      };
      this.$axios
        .post("/login", formData)
        .then((response) => {
          const accessToken = response.data.access_token;
          localStorage.setItem("access_token", accessToken);
          const user = response.data.user;
          localStorage.setItem("user", JSON.stringify(user));
          this.successAlertVisible = true;
          setTimeout(() => {
            this.$router.push("/dashboard");
          }, 2000); // Redirect after 2 seconds
        })
        .catch((error) => {
          this.errorAlertVisible = true;
          if (error.response && error.response.data && error.response.data.message) {
            this.errorMessage = error.response.data.message;
          } else {
            this.errorMessage = "An unknown error occurred";
          }
        });
    },
  },
};
</script>

<style scoped>
.signup-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.signup-form {
  text-align: center;
  background-color: #ffffff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 320px;
}

h2 {
  margin-bottom: 16px;
  font-size: 24px;
}

label {
  font-size: 14px;
  font-weight: bold;
  display: block;
  margin-bottom: 6px;
}

input[type="text"],
input[type="password"],
input[type="email"] {
  width: 80%;
  padding: 10px;
  margin-bottom: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
}

button {
  background-color: #007bff;
  color: #ffffff;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
