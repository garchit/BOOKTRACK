<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">MyApp</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link :to ="'/profile/' + this.user_id" class="nav-link">Profile</router-link>
          </li>
        </ul>
      </div>
    </nav>
    <h1>Sections </h1>
    <div class="row justify-content-center w-100">
      <table class="table table-striped " style="width:70% ">
        <thead>
          <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Created Date</th>
            <th>Options</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(section, index) in sections" :key="index" style="font-size:20px">
            <td>{{ section.name }}</td>
            <td>{{ section.description }}</td>
            <td>{{ formatDate(section.date_created) }}</td>
            <td>
              <router-link :to="'/userbooks/' + this.user_id +'/'+ section.id" class="btn btn-info mr-3">View Books</router-link>
              <!-- <button @click="confirmDelete(section)" class="btn btn-outline-danger ml-2 mr-2">Delete</button> -->
              <!-- <button @click="confirmDelete(section)" class="btn btn-outline-primary ml-2">Manage Books</button> -->
              <!-- <router-link to="/admin" class="btn btn-outline-primary ml-2">Manage Books</router-link> -->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <div v-if="sections.length === 0">
    <p>No books available.</p>
  </div>
  <!-- </div> -->
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      newSectionName: '',
      newSectionDescription: '',
      sections: [], // Corrected from 'sections' to 'books'
      editingSection: null,
      editedSectionName: '',
      editedSectionDescription: '',
      confirmingDelete: false,
      deletedSection: null,
      user_id : null
    }
  },
  mounted() {
    this.user_id = localStorage.getItem('user_id');
    this.fetchSections(); // Changed from fetchSections to fetchBooks
  },
  methods: {
    async fetchSections() {
      try {
        const response = await axios.get(process.env.VUE_APP_URL+'/sections');
        this.sections = response.data;
        console.log(response)
        // localStorage.setItem("section_details", this.sections.id);
        console.log(this.user_id)
      } catch (error) {
        console.error('Error fetching sections:', error);
      }
    },
    formatDate(date) {
      const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
      return new Date(date).toLocaleDateString(undefined, options);
    },

    // Other methods
  }
}
</script>

<style>
/* Add your CSS styles here */
</style>