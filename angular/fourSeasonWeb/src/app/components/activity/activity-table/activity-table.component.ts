import { AfterViewInit, Component, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTable } from '@angular/material/table';
import { ActivityTableDataSource, ActivityTableItem } from './activity-table-datasource';
import { ActivityService } from '../../../services/activity.service';
import { animate, state, style, transition, trigger } from '@angular/animations';

@Component({
  selector: 'app-activity-table',
  templateUrl: './activity-table.component.html',
  styleUrls: ['./activity-table.component.css'],
  animations: [
    trigger('detailExpand', [
      state('collapsed', style({ height: '0px', maxHeight: '0' })),
      state('expanded', style({ height: '*' })),
      transition('expanded <=> collapsed', animate('225ms cubic-bezier(0.4, 0.0, 0.2, 1)')),
    ]),
  ],
})
export class ActivityTableComponent implements AfterViewInit {
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;
  @ViewChild(MatTable) table!: MatTable<ActivityTableItem>;
  dataSource: ActivityTableDataSource;
  leaders: string[] = [];

  displayedColumns = [
    'title',
    'get_leaders',
    'trip_date',
    'get_activity_type_display',
    'activity_requirements',
    'activity_apply'
  ];

  constructor(private _servcie: ActivityService) {
    this.dataSource = new ActivityTableDataSource();
  }

  ngAfterViewInit(): void {
    this._servcie.GetActivity().subscribe(data => {
      this.dataSource = new ActivityTableDataSource();
      this.dataSource.data = this.addIsExpanded(data.results);
      this.dataSource.sort = this.sort;
      this.dataSource.paginator = this.paginator;
      this.table.dataSource = this.dataSource;
    })
  }

  addIsExpanded(data: Array<ActivityTableItem>): Array<ActivityTableItem> {
    data.forEach(element => (element.isExpanded = false))
    return data;
  }

  toggleRow(row: any) {
    console.log("toggle")
    console.log(row)
    row.isExpanded = !row.isExpanded;
  }

  splitUser(input: string) {
    return input.split(" ");
  }
}
