import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Router } from '@angular/router';

import { User } from '../auth-components/user';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  endpoint: string = 'http://localhost:8081';
  headers = new HttpHeaders().set('Content-Type', 'application/json');
  currentUser = {};

  constructor(
    private http: HttpClient,
    public router: Router
  ) { }

  // Sign-up
  signUp(user: User): Observable<any> {
    let api = `${this.endpoint}/api/auth/users/`;
    return this.http.post(api, user)
      .pipe(
        catchError(this.handleError)
      )
  }

  // Sign-in
  signIn(user: User) {
    return this.http.post<any>(`${this.endpoint}/api/auth/login/`, user)
      .subscribe((res: any) => {
        localStorage.setItem('access_token', res.token)
        localStorage.setItem('username', res.user["username"])
        this.router.navigate(["/"])
      })
  }

  registerUser(user: User) {
    let url = `${this.endpoint}/api/auth/register/`
    return this.http.post<any>(url, user)
    .pipe(
      catchError(this.handleError)
    );
  }

  getToken() {
    return localStorage.getItem('access_token');
  }

  get isLoggedIn(): boolean {
    let authToken = localStorage.getItem('access_token');
    return (authToken !== null) ? true : false;
  }

  doLogout() {
    localStorage.clear();
    this.router.navigate(["home"]);
  }

  // User profile
  getUserProfile(id: string): Observable<any> {
    let api = `${this.endpoint}/api/auth/users/${id}`;
    return this.http.get<any>(api, { headers: this.headers }).pipe(
      map((res: Response) => {
        return res || {}
      }),
      catchError(this.handleError)
    )
  }

  // Error
  handleError(error: HttpErrorResponse) {
    let msg = '';
    if (error.error instanceof ErrorEvent) {
      // client-side error
      msg = error.error.message;
    } else {
      // server-side error
      msg = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }
    return throwError(msg);
  }
}
