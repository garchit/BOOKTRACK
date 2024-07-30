<template>
    <div>
        <h1>I am Managing differnt books </h1>
        <div v-if="sections.length > 0">
            <h3>Sections</h3>
            <table class="table table-striped table-hover">
                <thead>
                    <tr>
                        <th scope="col">Name</th>
                        <th scope="col">Description</th>
                        <th scope="col">Created Date</th>
                        <th scope="col">Options</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(section, index) in sections" :key="index">
                        <td>{{ section.name }}</td>
                        <td>{{ section.description }}</td>
                        <td>{{ formatDate(section.date_created) }}</td>
                        <td>
                            <!-- <button class = "btn btn-warning">Add books</button> -->
                            <!-- <router-link to="{ name: 'addbook', params: { section_id: section.id } }" class="btn btn-warning">Add Books</router-link> -->
                            <!-- <router-link :to="'/storebooks/' + section.id" class="btn btn-info mr-3">View
                                Books</router-link> -->
                            <button class="btn btn-info mr-2" @click="handleViewBook(section.id)">view Books</button>

                            <button class="btn btn-warning" @click="handleAddBook(section.id)">Add Books</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div v-else>
            <p>No sections available.</p>
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
        }
    },
    mounted() {
        this.fetchSections();
    },
    methods: {
        async fetchSections() {
            try {
                const response = await axios.get('/sections');
                this.sections = response.data;
            } catch (error) {
                console.error('Error fetching sections:', error);
            }
        },
        formatDate(date) {
            const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
            return new Date(date).toLocaleDateString(undefined, options);
        },

        handleAddBook(sectionId) {
            // Store sectionId in localStorage
            localStorage.setItem('sectionId', sectionId);

            // Redirect to the add book page
            this.$router.push(`/addbook/${sectionId}`);
            // localStorage.removeItem('sectionId')
        },
        handleViewBook(sectionId) {
            localStorage.setItem("sectionId", sectionId)
            this.$router.push(`/storebooks/${sectionId}`);

        }
        // Other methods
    }
}
</script>

<style></style>