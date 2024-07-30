<!-- HomePage.vue -->

<template>
  <div class="home-container">
    <h1>Welcome to the BOOKTRACK</h1>
    <div class="actions">
      <router-link to="/signup" class="action-btn">Sign Up</router-link>
      <router-link to="/userlogin" class="action-btn">login now </router-link>
      <!-- <router-link to="/transactions" class="action-btn">View Transactions</router-link> -->
      <router-link to="/admin" class="action-btn">Admin login</router-link>

    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeWorld'
};
</script>

<style scoped>
.home-container {
  text-align: center;
  padding: 50px;
}

.actions {
  margin-top: 30px;
}

.action-btn {
  display: inline-block;
  margin: 0 10px;
  padding: 10px 20px;
  font-size: 18px;
  background-color: #007bff;
  color: #fff;
  text-decoration: none;
  border-radius: 5px;
  cursor: pointer;
}

.action-btn:hover {
  background-color: #0056b3;
}
</style>



