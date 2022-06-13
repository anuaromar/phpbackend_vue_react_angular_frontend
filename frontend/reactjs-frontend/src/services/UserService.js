import axios from 'axios';

//const USER_API_URL = "http://localhost:8888/php-mysql-crud-api";
const USER_API_URL = 'http://127.0.0.1:5000'

class UserService {

    getUsers(){
        //return axios.get(`${USER_API_URL}/read.php`);
        return axios.get(`${USER_API_URL}/read`);
    }

    createUser(user){
        //return axios.post(`${USER_API_URL}/create.php`, user);
        return axios.post(`${USER_API_URL}/create`, user);
    }

    getUserById(id){
        // return axios.get(`${USER_API_URL}/single_user.php`, 
        //     { params: { id: id } });
        return axios.get(`${USER_API_URL}/single_user`, 
            { params: { id: id } });
    }

    updateUser(user){
        // return axios.put(`${USER_API_URL}/update.php`, user);
        return axios.put(`${USER_API_URL}/update`, user);
    }

    deleteUser(id){
        // return axios.delete(`${USER_API_URL}/delete.php`, 
        //                             { params: { id: id } });
        return axios.delete(`${USER_API_URL}/delete`, 
        { params: { id: id } });
    }
}

export default new UserService()