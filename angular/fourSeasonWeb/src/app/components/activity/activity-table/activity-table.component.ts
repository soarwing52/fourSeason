import { AfterViewInit, Component, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTable } from '@angular/material/table';
import { ActivityTableDataSource, ActivityTableItem } from './activity-table-datasource';
import {ActivityService} from '../../../services/activity.service';

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
  leaders : string[] = [];

  /** Columns displayed in the table. Columns IDs can be added, removed, or reordered. */
  displayedColumns = [
    'title',
    'content',
    'get_leaders',
    'trip_date',
    'get_activity_type_display',
    'activity_requirements',
  ];

  constructor(private _servcie: ActivityService) {
    this.dataSource = new ActivityTableDataSource();
  }

  ngAfterViewInit(): void {
    this._servcie.GetActivity().subscribe(data => {
      this.dataSource = new ActivityTableDataSource();
      this.dataSource.data = data.results;
      this.dataSource.sort = this.sort;
      this.dataSource.paginator = this.paginator;
      this.table.dataSource = this.dataSource;
    })
  }

  splitUser(input: string){
    return input.split(" ");
  }
}
