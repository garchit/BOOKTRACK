<template>
    <h1> Add new section here </h1>
     <!-- Create Section Form -->
     <div class="mb-4">
        <h3>Create Section</h3>
        <form @submit.prevent="createSection" class="form">
          <div class="mb-3">
            <label for="sectionName" class="form-label">Section Name:</label>
            <input type="text" id="sectionName" v-model="newSectionName" required class="form-control">
          </div>
          <div class="mb-3">
            <label for="sectionDescription" class="form-label">Description:</label>
            <textarea id="sectionDescription" v-model="newSectionDescription" class="form-control"></textarea>
          </div>
          <button type="submit" class="btn btn-primary">Create Section</button>
        </form>
      </div>
</template>

<script>
import axios from 'axios';

export default{
    data(){
        return{
        newSectionName: '',
        newSectionDescription: '',
        sections: [],
        editingSection: null,
        editedSectionName: '',
        editedSectionDescription: '',
        confirmingDelete: false,
        deletedSection: null,            
        }
    },
    // mounted() {
    //   this.fetchSections();
    // },
    methods:{
        async createSection() {
        try {
          const response = await axios.post('/sections', {
            name: this.newSectionName,
            description: this.newSectionDescription,
          });
          console.log(response.data);
        //   this.fetchSections();
        //   window.location.reload();
          this.$router.push("/adminDashboard");
        } catch (error) {
          console.error('Error creating section:', error);
        }
      }
    }
}


</script>

