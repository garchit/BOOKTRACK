<template>
    <div>
        <h2>New login Form </h2>
        <form @submit.prevent="handleLogin">

            <label for="username">Username</label>
            <input type="text" id="username" v-model="username" required />

            <label for="password">Password</label>
            <input type="password" id="password" v-model="password" required />

            <button type="submit">Submit</button>

        </form>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            username: "",
            password: ""
        }
    },
    methods: {
        async handleLogin() {
            try {
                console.log(process.env.VUE_APP_URL);
                console.log(process.env.VUE_APP_URL+"userlogin")
                const response = await axios.post(process.env.VUE_APP_URL+"/userlogin", {
                    username: this.username,
                    password: this.password
                });

                localStorage.setItem('access_token', response.data.access_token)
                localStorage.setItem('userRole', response.data.userRole)
                localStorage.setItem('isauthenticated', true);
                localStorage.setItem('username', response.data.username);
                localStorage.setItem('user_id',response.data.user_id)
                // this.$router.push('/dashboard');

                if (response.data.userRole === 'admin') {
                    this.$router.push('/adminDashboard');
                } else {
                    // this.$router.push('/UserSection');
                    this.$router.push(`/usersection/${response.data.user_id}`);
                }


            }

            catch (error) {
                console.error(error.message)
            }
        }
    }
}
</script>