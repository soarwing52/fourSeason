import { AfterViewInit, Component, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTable } from '@angular/material/table';
import { ActivityTableDataSource, ActivityTableItem } from './activity-table-datasource';
import {ActivityService} from '../../services/activity.service';

@Component({
  selector: 'app-activity-table',
  templateUrl: './activity-table.component.html',
  styleUrls: ['./activity-table.component.css']
})
export class ActivityTableComponent implements AfterViewInit {
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;
  @ViewChild(MatTable) table!: MatTable<ActivityTableItem>;
  dataSource: ActivityTableDataSource;

  /** Columns displayed in the table. Columns IDs can be added, removed, or reordered. */
  displayedColumns = ['title', 'content'];

  constructor(private _servcie: ActivityService) {
    this.dataSource = new ActivityTableDataSource();
    this._servcie.GetActivity().subscribe(data => {
      console.log(data.results);
      this.dataSource = new ActivityTableDataSource();
      this.dataSource.data = data.results;
      this.dataSource.sort = this.sort;
      this.dataSource.paginator = this.paginator;
      this.table.dataSource = this.dataSource;
    })
  }

  ngAfterViewInit(): void {
    this.dataSource.sort = this.sort;
    this.dataSource.paginator = this.paginator;
    this.table.dataSource = this.dataSource;
  }
}
