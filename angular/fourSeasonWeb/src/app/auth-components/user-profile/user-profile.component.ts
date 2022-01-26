import { Component, OnInit } from '@angular/core';
import {ActivatedRoute } from '@angular/router';
import {AuthService} from '../../services/auth.service';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {

  currentUser = {
    "name": "new",
    "email": "email@example.com"
  };

  constructor(
    public authService: AuthService,
    private actRoute: ActivatedRoute
  ) {
    this.currentUser["name"] = "name";
    this.currentUser["email"] = "email";
    let id = this.actRoute.snapshot.paramMap.get('id');
    console.log(id);
    // this.authService.getUserProfile(id).subscribe(res => {
    //   this.currentUser = {
    //     "name": "new",
    //     "email": "email@example.com"
    //   };
    // })
  }

  ngOnInit(): void {
  }

}
