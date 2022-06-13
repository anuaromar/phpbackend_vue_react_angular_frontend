import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  // private baseUrl = 'http://localhost:8888/php-mysql-crud-api';
  private baseUrl = 'http://127.0.0.1:5000';

  constructor(private http: HttpClient) { }

  getUser(id: string): Observable<any> {
    // return this.http.get(`${this.baseUrl}/single_user.php`,
    // { params: { id: id } });
    return this.http.get(`${this.baseUrl}/single_user`,
    { params: { id: id } });
  }

  createUser(user: Object): Observable<Object> {
    // return this.http.post(`${this.baseUrl}/create.php`, user);
    return this.http.post(`${this.baseUrl}/create`, user);
  }

  updateUser(user: Object): Observable<Object> {
    //return this.http.put(`${this.baseUrl}/update.php`, user);
    return this.http.put(`${this.baseUrl}/update`, user);
  }

  deleteUser(id: string): Observable<any> {
    // return this.http.delete(`${this.baseUrl}/delete.php`,
    // { params: { id: id } },
    // );
    return this.http.delete(`${this.baseUrl}/delete`,
    { params: { id: id } },
    );

  }

  getUsersList(): Observable<any> {
    // return this.http.get(`${this.baseUrl}/read.php`);
    return this.http.get(`${this.baseUrl}/read`);
  }
}