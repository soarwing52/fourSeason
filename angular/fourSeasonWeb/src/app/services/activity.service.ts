import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ActivityService {
  baseUrl = 'http://localhost:8081';

  constructor(private http: HttpClient) { }

  GetActivity(){
    const connectUrl = `${this.baseUrl}/activities/activities/`;
    return this.http.get<any>(connectUrl);
  }
}
