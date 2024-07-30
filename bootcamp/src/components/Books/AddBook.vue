 <!-- <template>
    <div>
      <h2>Add New Book</h2>
      <form @submit.prevent="addBook">
        <div>
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="book.name" required>
        </div>
        <div>
          <label for="content">Content:</label>
          <textarea id="content" v-model="book.content" required></textarea>
        </div>
        <div>
          <label for="author">Author:</label>
          <input type="text" id="author" v-model="book.author" required>
        </div>
        <div>
          <label for="price">Price:</label>
          <input type="number" id="price" v-model="book.price">
        </div>
        <div>
          <label for="poster">Poster:</label>
          <input type="text" id="poster" v-model="book.poster">
        </div>
       
        <button type="submit">Add Book</button>
      </form>
    </div>
  </template>
 
  <script>
  import axios from 'axios';
  
  export default {
    
    data() {
      return {
        book: {
          name: '',
          content: '',
          author: '',
          price: null,
          poster: '',
          section_id: localStorage.getItem("sectionId")

        }
      };
    },
    methods: {
      async addBook() {
        try {
          const formData = new FormData();
          formData.append('name', this.book.name);
          formData.append('content', this.book.content);
          formData.append('author', this.book.author);
          formData.append('price', this.book.price);
          formData.append('poster', this.book.poster);
        console.log("yha tkk"),
        console.log("section id " , this.book.section_id)
          await axios.post(`/sections/${this.book.section_id}/books`, formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
          alert('Book added successfully!');
          this.$router.push(`/storebooks/${this.book.section_id}`)
        } catch (error) {
          console.error('Error adding book:', error);
          alert('Failed to add book. Please try again.');
        }
      }
   
    }
  
  
};
  </script>


   



   -->


   <template>
    <div class="container mt-4">
      <h2>Add New Book</h2>
      <form @submit.prevent="addBook" class="needs-validation" novalidate>
        <div class="mb-3">
          <label for="name" class="form-label">Name:</label>
          <input type="text" id="name" v-model="book.name" class="form-control" required>
          <div class="invalid-feedback">Name is required</div>
        </div>
        <div class="mb-3">
          <label for="content" class="form-label">Content:</label>
          <textarea id="content" v-model="book.content" class="form-control" required></textarea>
          <div class="invalid-feedback">Content is required</div>
        </div>
        <div class="mb-3">
          <label for="author" class="form-label">Author:</label>
          <input type="text" id="author" v-model="book.author" class="form-control" required>
          <div class="invalid-feedback">Author is required</div>
        </div>
        <div class="mb-3">
          <label for="price" class="form-label">Price:</label>
          <input type="number" id="price" v-model="book.price" class="form-control">
        </div>
        <div class="mb-3">
          <label for="poster" class="form-label">Poster:</label>
          <input type="text" id="poster" v-model="book.poster" class="form-control">
        </div>
        <button type="submit" class="btn btn-primary">Add Book</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        book: {
          name: '',
          content: '',
          author: '',
          price: null,
          poster: '',
          section_id: localStorage.getItem("sectionId")
        }
      };
    },
    methods: {
      async addBook() {
        try {
          const formData = new FormData();
          formData.append('name', this.book.name);
          formData.append('content', this.book.content);
          formData.append('author', this.book.author);
          formData.append('price', this.book.price);
          formData.append('poster', this.book.poster);
  
          await axios.post(`/sections/${this.book.section_id}/books`, formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
          alert('Book added successfully!');
          this.$router.push(`/storebooks/${this.book.section_id}`);
        } catch (error) {
          console.error('Error adding book:', error);
          alert('Failed to add book. Please try again.');
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add any custom scoped styles here if needed */
  </style>
  