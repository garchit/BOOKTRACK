<!-- <template>
  <div>
      <h2>Signup</h2>
      <form @submit.prevent="signup">
          
          <label for="username">Username</label>
          <input type="text" id="username" v-model="username" required />

          <label for="password">Password</label>
          <input type="password" id="password" v-model="password" required />

          <button type="submit">Signup</button>

      </form>
  </div>
</template>

<script>
import axios from 'axios';
import { useToast } from 'vue-toastification';
export default {
  data() {
    return {
      username: '',
      password: '',
      role: 'user',
    };
  },
  setup() {
    const toast = useToast();
    return { toast };
  },
  methods: {
    
    async signup() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/signup', {
          username: this.username,
          password: this.password,
          role: this.role,
        });
        console.log('Signup Successful', response.data);
        this.toast.success('Signup successful!');
        this.$router.push("/userlogin");
      } catch(error) {
        console.error('Signup Error:', error);
        this.toast.error('Signup failed. Please try again.');
      }
    }
  }
}
</script>

<style>
</style> -->


<template>
  <div>
    <h2>Signup</h2>
    <form @submit.prevent="signup">
      <label for="username">Username</label>
      <input type="text" id="username" v-model="username" required />

      <label for="password">Password</label>
      <input type="password" id="password" v-model="password" required />

      <button type="submit">Signup</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import { useToast } from 'vue-toastification';

export default {
  data() {
    return {
      username: '',
      password: '',
      role: 'user',
    };
  },
  setup() {
    const toast = useToast();
    return { toast };
  },
  methods: {
    async signup() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/signup', {
          username: this.username,
          password: this.password,
          role: this.role,
        });
        console.log('Signup Successful', response.data);
        this.toast.success('Signup successful!');
        this.$router.push("/userlogin");
      } catch (error) {
        console.error('Signup Error:', error);
        this.toast.error('Signup failed. Please try again.');
      }
    }
  },
  created() {
    const { toast } = this.$options.setup();
    this.toast = toast;
  }
}
</script>

<style>
/* Add any desired styles here */
</style>
