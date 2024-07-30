<!-- <template>
  <div class="library">
    <header>
      <h1>Welcome to Our Library</h1>
    </header>
    <div class="book-list">
      <div v-for="(book, index) in books" :key="index" class="book">
        <div class="book-cover">
          <img :src="book.cover" :alt="book.title" />
        </div>
        <div class="book-details">
          <h2>{{ book.title }}</h2>
          <p>Author: {{ book.author }}</p>
          <p>Genre: {{ book.genre }}</p>
          <p>Published Year: {{ book.publishedYear }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      books: [
        { title: 'Book 1', author: 'Author 1', genre: 'Fiction', publishedYear: 2000, cover: 'https://cdn-icons-png.flaticon.com/128/3038/3038089.png' },
        { title: 'Book 2', author: 'Author 2', genre: 'Non-fiction', publishedYear: 2010, cover: 'https://via.placeholder.com/150' },
        { title: 'Book 3', author: 'Author 3', genre: 'Science', publishedYear: 2020, cover: 'https://via.placeholder.com/150' }
        // Add more books as needed
      ]
    };
  }
};
</script>

<style scoped>
.library {
  font-family: Arial, sans-serif;
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

header {
  text-align: center;
  margin-bottom: 20px;
}

.book-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  grid-gap: 20px;
}

.book {
  background-color: #f9f9f9;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.book:hover {
  transform: translateY(-5px);
}

.book-cover img {
  width: 100%;
  height: auto;
  border-bottom: 1px solid #ddd;
}

.book-details {
  padding: 10px;
}

.book-details h2 {
  font-size: 1.2rem;
  margin-bottom: 5px;
}

.book-details p {
  margin: 5px 0;
}
</style> -->


<template>
  <div>
      <nav class="navbar">

          <div class="navbar-brand">
              <h1 class="title">Library </h1>
          </div>
          <div class="navbar-menu">
              <div class="navbar-end">
                  <router-link to="/" class="navbar-item"> Home</router-link>
                  <router-link v-if="isauthenticated" to="/userlogin" class="navbar-item"> Login</router-link>
                  <router-link v-if="isauthenticated" to="/signup" class="navbar-item"> Signup</router-link>
                  <router-link v-if="isauthenticated && isAdmin" to="/dashboard" class="navbar-item"> Dashboard</router-link>
                  <button v-if="!isauthenticated" @click="logout" class="navbar-item"> Logout</button>
                  
              </div>
          </div>
      </nav>

      <div>
          <h2>Read Borrow Learn</h2>
      </div>
      <div class="section-list">
        <div v-if="sections.length > 0">
          <div v-for="(section, index) in sections" :key="index" class="section">
            <h2>{{ section.name }}</h2>
            <p>{{ section.description }}</p>
            <p>Created Date: {{ section.date_created }}</p>
            <!-- You can display additional information if needed -->
          </div>
        </div>
        <div v-else>
          <p>No sections available.</p>
        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      sections: []
    };
  },
  mounted() {
    this.fetchSections();
  },
  methods: {
    async fetchSections() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/sections');
        this.sections = response.data;
      } catch(error) {
        console.error('Error fetching sections:', error);
      }
    },
    logout(){
            // const access_token = localStorage.getItem('access_token');
            // this.$axios.post('http://127.0.0.1:8000/logout',null,{
            //     headers:{
            //         Authorization: `Bearer ${access_token}`
            //     }
            // })

            // .then(()=>{
                localStorage.removeItem('access_token');
                localStorage.removeItem('userRole');
                localStorage.setItem('isauthenticated',false);
                this.isauthenticated = false;
                this.$router.push("/")
            // })
        },
  }
}
</script>