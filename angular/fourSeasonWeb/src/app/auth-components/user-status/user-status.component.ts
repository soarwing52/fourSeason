import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-user-status',
  templateUrl: './user-status.component.html',
  styleUrls: ['./user-status.component.css']
})
export class UserStatusComponent implements OnInit {
  isLoggedIn: boolean = false;
  username: string | null = "";

  constructor(private authService: AuthService) {
  }

  ngOnInit(): void {
    this.authService.router.events.subscribe(event => {
      if (event.constructor.name === "NavigationEnd") {
        this.isLoggedIn = this.authService.isLoggedIn;
        this.username = localStorage.getItem('username');
      }
    })
  }



  LogOut() {
    this.authService.doLogout();
  }

  LogIn() {
    this.authService.router.navigate(["log-in"]);
  }
}
