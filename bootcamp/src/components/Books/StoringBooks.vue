<template>
  <div>
    <h1>Books</h1>
        <!-- Search Section -->
        <div class="search-container">
          <input type="text" v-model="searchTerm" placeholder="Search books" class="form-control mb-3" style="width: 50%; text-align: center;">
          <button @click="fetchSearchBooks" class="btn btn-primary">Search</button>
        </div>
    <div class="container">
      <div class="row">
        <div v-for="book in books" :key="book.id" class="col-md-4 mb-4">
          <div class="card">
            <img :src="book.poster" class="card-img-top" alt="Book Cover" height="300px" width="300px">
            <div class="card-body">
              <h5 class="card-title">{{ book.name }}</h5>
              <p class="card-text">Author - {{ book.author }}</p>
              <p class="card-text">Price - {{ book.price }}</p>
              <button class="btn btn-primary mr-3" @click="openUpdateOverlay(book)">Update Book</button>
              <button class="btn btn-danger" @click="openDeleteOverlay(book)">Delete Book</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="books.length === 0">
      <p>No books available.</p>
    </div>

    <!-- Update Overlay -->
    <div v-if="showUpdateOverlay" class="overlay">
      <div class="overlay-content">
        <h2>Update Book</h2>
        <form @submit.prevent="updateBook">
          <label for="name">Name:</label>
          <input type="text" v-model="editBook.name" required>
          <label for="content">Content:</label>
          <textarea v-model="editBook.content" required></textarea>
          <label for="author">Author:</label>
          <input type="text" v-model="editBook.author" required>
          <label for="price">Price:</label>
          <input type="number" v-model="editBook.price" required>
          <label for="poster">Poster:</label>
          <input type="text" v-model="editBook.poster">
          <button type="submit" class="btn btn-primary">Save</button>
          <button class="btn btn-secondary" @click="closeOverlay">Cancel</button>
        </form>
      </div>
    </div>

    <!-- Delete Overlay -->
    <div v-if="showDeleteOverlay" class="overlay">
      <div class="overlay-content">
        <h2>Delete Book</h2>
        <p>Are you sure you want to delete "{{ deleteBookData.name }}"?</p>
        <button class="btn btn-danger" @click="deleteBook">Delete</button>
        <button class="btn btn-secondary" @click="closeOverlay">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      books: [],
      showUpdateOverlay: false,
      showDeleteOverlay: false,
      editBook: {
        id: null,
        name: '',
        content: '',
        author: '',
        price: '',
        poster: '',

      },
      deleteBookData: null,
      section_id: localStorage.getItem("sectionId")
    };
  },
  mounted() {
    this.fetchBooks();
  },
  methods: {
    async fetchBooks() {
      try {
        const response = await axios.get(`/storebooks/${this.$route.params.section_id}`);
        this.books = response.data;
        console.log("book is -", response)
      } catch (error) {
        console.error('Error fetching books:', error);
      }
    },
    async fetchSearchBooks() {
      try {
        const response = await axios.get(`/storebooks/${this.$route.params.section_id}?search=${this.searchTerm}`);
        this.books = response.data;
        console.log("Searched books:", response);
      } catch (error) {
        console.error('Error searching books:', error);
      }
    },
    openUpdateOverlay(book) {
      this.editBook = { ...book }; // Clone book object to avoid mutating the original data
      this.showUpdateOverlay = true;
    },
    openDeleteOverlay(book) {
      this.deleteBookData = book;
      this.showDeleteOverlay = true;
    },
    async updateBook() {
      try {
        console.log('editBook:', this.editBook);
        console.log("section id", this.section_id)
        await axios.put(`/books/${this.section_id}/${this.editBook.id}`, this.editBook);
        this.closeOverlay();
        this.fetchBooks();
      } catch (error) {
        console.error('Error updating book:', error);
      }
    },
    async deleteBook() {
      try {
        console.log("working")
        await axios.delete(`/books/${this.section_id}/${this.deleteBookData.id}`);
        this.closeOverlay();
        this.fetchBooks();
      } catch (error) {
        console.error('Error deleting book:', error);
      }
    },
    closeOverlay() {
      this.showUpdateOverlay = false;
      this.showDeleteOverlay = false;
    }
  }
};
</script>

<style scoped>
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.overlay-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
}

.overlay form {
  margin-bottom: 0;
}
</style>
