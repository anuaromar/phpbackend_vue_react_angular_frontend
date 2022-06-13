<template>
  <div class="container">
    <div class="navbar-header">
      <a class="navbar-brand" href="http://localhost:9080/users">PHP + MYSQL + VUE CRUD Application</a><br/><br/>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: "app"
};
</script>

<style>
@import url(https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css);

</style>
