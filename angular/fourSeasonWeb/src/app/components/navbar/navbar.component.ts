import { Component, OnInit, ViewChild } from '@angular/core';
import { MatMenuTrigger } from '@angular/material/menu';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  @ViewChild(MatMenuTrigger)
  trigger!: MatMenuTrigger;

  someMethod() {
    console.log('someMethod')
    this.trigger.openMenu();
  }
  constructor() { }

  ngOnInit(): void {
    // setTimeout(() =>{
    //   this.someMethod()
    // }, 2000)
  }

}
