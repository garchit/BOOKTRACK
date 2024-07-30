<!-- BookDetail.vue -->
<template>
  <div class="container mt-4">
    <h2>{{ book.name }}</h2>
    <p><strong>Author:</strong> {{ book.author }}</p>
    <p><strong>Price:</strong> {{ book.price }}</p>
    <p><strong>Content:</strong></p>
    <div class="book-content">
      {{ book.content }}
    </div>
    <p><strong>Issue Date:</strong> {{ formatDate(book.issue_date) }}</p>
    <img v-if="book.poster" :src="book.poster" alt="Book Poster" class="img-fluid">
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      book: {}
    };
  },
  created() {
    this.fetchBook();
  },
  methods: {
    async fetchBook() {
      try {
        const bookId = localStorage.getItem('bookId');
        console.log(bookId); // Log the book ID for debugging
        const response = await axios.get(`/books/${bookId}`); // Adjust API endpoint as per your backend setup
        this.book = response.data; // Assuming your API returns book details including content
      } catch (error) {
        console.error('Error fetching book:', error);
        alert('Failed to fetch book details.');
      }
    },
    formatDate(dateStr) {
      return new Date(dateStr).toLocaleDateString(); // Adjust date formatting as needed
    }
  }
};
</script>

<style scoped>
.book-content {
  white-space: pre-line; /* Preserve line breaks in content */
}
</style>
