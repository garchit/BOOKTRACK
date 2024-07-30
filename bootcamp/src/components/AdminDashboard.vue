<template>
  <div>
    <h2 class="mb-4">Manage Sections</h2>
    <div class="actions">
      <router-link to="/addsection" class="btn btn-primary mr-3">Add section</router-link>
      <router-link to="/managebook" class="btn btn-primary mr-3">Manage Sections</router-link>
      <router-link to="/userbookaccess" class="btn btn-primary">Requested Books </router-link>
    </div>
    <div>
      <input type="text" v-model="searchTerm" placeholder="Search sections" class="form-control mb-3" style="width: 50%; text-align: center;">
      <button @click="fetchSearchSections">Search</button>
    </div>
    <!-- Section List -->
      <div v-if="sections.length > 0">
        <h3>Sections</h3>
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
              <tr v-for="(section, index) in sections" :key="index" style="font-size:22px">
                <td>{{ section.name }}</td>
                <td>{{ section.description }}</td>
                <td>{{ formatDate(section.date_created) }}</td>
                <td>
                  <button @click="editSection(section)" class="btn btn-outline-primary mr-2">Edit</button>
                  <button @click="confirmDelete(section)" class="btn btn-outline-danger ml-2 mr-2">Delete</button>
                  <!-- <button @click="confirmDelete(section)" class="btn btn-outline-primary ml-2">Manage Books</button> -->
                  <!-- <router-link to="/admin" class="btn btn-outline-primary ml-2">Manage Books</router-link> -->
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div v-else>
        <p>No sections available.</p>
      </div>

      <!-- Edit Section Form -->


      <div v-if="editingSection" class="overlay">
        <div class="overlay-content">
          <h3>Edit Section</h3>
          <form @submit.prevent="saveEdit" class="form">
            <div class="mb-3">
              <label for="editedSectionName" class="form-label">Section Name:</label>
              <input type="text" id="editedSectionName" v-model="editedSectionName" required class="form-control">
            </div>
            <div class="mb-3">
              <label for="editedSectionDescription" class="form-label">Description:</label>
              <textarea id="editedSectionDescription" v-model="editedSectionDescription"
                class="form-control"></textarea>
            </div>
            <button type="submit" class="btn btn-primary me-2 mr-2">Save</button>
            <button @click="cancelEdit" class="btn btn-secondary">Cancel</button>
          </form>
        </div>
      </div>
      <!-- </div> -->

      <!-- Confirm Delete Section -->
      <div v-if="confirmingDelete" class="overlay">
        <div class="overlay-content">
          <h3>Confirm Delete</h3>
          <p>Are you sure you want to delete this section?</p>
          <button @click="deleteSection" class="btn btn-danger me-2 mr-2">Yes, Delete</button>
          <button @click="cancelDelete" class="btn btn-secondary">Cancel</button>
        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      newSectionName: '',
      newSectionDescription: '',
      sections: [],
      editingSection: null,
      editedSectionName: '',
      editedSectionDescription: '',
      confirmingDelete: false,
      deletedSection: null,
      searchQuery: '',
    };
  },
  mounted() {
    this.fetchSections();
    // this.fetchSearchSections();
  },
  methods: {
    async fetchSections() {
      try {
        const response = await axios.get('/sections');
        this.sections = response.data;
        // localStorage.setItem("section_details", this.sections.id);
      } catch (error) {
        console.error('Error fetching sections:', error);
      }
    },
    async fetchSearchSections() {
      try {
        console.log("I am working ")
        const response = await axios.get(`/sections?search=${this.searchTerm}`);       
         this.sections = response.data;
      } catch (error) {
        console.error('Error fetching sections:', error);
      }
    },
    async createSection() {
      try {
        const response = await axios.post('/sections', {
          name: this.newSectionName,
          description: this.newSectionDescription,
        });
        console.log(response.data);
        this.fetchSections();
        window.location.reload();
      } catch (error) {
        console.error('Error creating section:', error);
      }
    },
    editSection(section) {
      this.editingSection = section.id;
      this.editedSectionName = section.name;
      this.editedSectionDescription = section.description;
    },
    async saveEdit() {
      try {
        const response = await axios.put(`/sections/${this.editingSection}`, {
          name: this.editedSectionName,
          description: this.editedSectionDescription,
        });
        console.log(response.data);
        this.fetchSections();
        this.cancelEdit();
      } catch (error) {
        console.error('Error saving edit:', error);
      }
    },
    cancelEdit() {
      this.editingSection = null;
      this.editedSectionName = '';
      this.editedSectionDescription = '';
    },
    confirmDelete(section) {
      this.confirmingDelete = true;
      this.deletedSection = section;
    },
    async deleteSection() {
      try {
        const response = await axios.delete(`/sections/${this.deletedSection.id}`);
        console.log(response.data);
        this.fetchSections();
        this.confirmingDelete = false;
      } catch (error) {
        console.error('Error deleting section:', error);
      }
    },
    cancelDelete() {
      this.confirmingDelete = false;
      this.deletedSection = null;
    },
    formatDate(dateString) {
      return new Date(dateString).toLocaleDateString();
    }
  },
};
</script>

<style scoped>
/* Additional Custom Styles */
.table-striped tbody tr:nth-of-type(odd) {
  background-color: #f7f7f7;
}

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

.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  /* Semi-transparent black */
  display: flex;
  justify-content: center;
  align-items: center;
}

.overlay-content {
  background-color: white;
  padding: 40px;
  /* Increased padding for more space */
  border-radius: 10px;
  /* Increased border radius for a smoother look */
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
  /* Increased box shadow for depth */
  max-width: 80%;
  position: relative;
  /* Ensure the overlay content is positioned relative to its parent */
  z-index: 1000;
  /* Set a high z-index value to ensure the overlay appears on top */
  /* Limiting maximum width to 80% of the viewport */
}

.overlay-form-label {
  font-weight: bold;
  /* Make form labels bold for better visibility */
  margin-bottom: 10px;
  /* Add some spacing below form labels */
}

.overlay-form-input {
  width: 100%;
  /* Make form inputs span the full width of the overlay */
  margin-bottom: 20px;
  /* Add some spacing below form inputs */

}
</style>