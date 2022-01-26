import { DataSource } from '@angular/cdk/collections';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { map } from 'rxjs/operators';
import { Observable, of as observableOf, merge } from 'rxjs';

// TODO: Replace this with your own data model type
export interface ActivityTableItem {
  title: string;
  content: string;
  created_on: string;
  due_date: string;
  get_leaders: string;
}

// TODO: replace this with real data from your application
const EXAMPLE_DATA: ActivityTableItem[] =  [
  {
      "title": "帖比倫",
      "content": "行程內容",
      "created_on": "2022-01-21",
      "due_date": "2022-01-21",
      "get_leaders": "admin"
  },
  {
      "title": "二子山",
      "content": "溫泉野溪",
      "created_on": "2022-01-21",
      "due_date": "2022-01-21",
      "get_leaders": "admin"
  },
  {
      "title": "拉卡溫泉",
      "content": "放鬆泡湯",
      "created_on": "2022-01-21",
      "due_date": "2022-01-21",
      "get_leaders": ""
  },
  {
      "title": "秀巒",
      "content": "嚮導訓練",
      "created_on": "2022-01-21",
      "due_date": "2022-01-21",
      "get_leaders": ""
  },
  {
      "title": "進階營",
      "content": "訓練",
      "created_on": "2022-01-21",
      "due_date": "2022-01-21",
      "get_leaders": ""
  },
  {
      "title": "進階營2",
      "content": "訓練",
      "created_on": "2022-01-21",
      "due_date": "2022-01-21",
      "get_leaders": ""
  }
]

/**
 * Data source for the ActivityTable view. This class should
 * encapsulate all logic for fetching and manipulating the displayed data
 * (including sorting, pagination, and filtering).
 */
export class ActivityTableDataSource extends DataSource<ActivityTableItem> {
  data: ActivityTableItem[] = [];
  paginator: MatPaginator | undefined;
  sort: MatSort | undefined;

  constructor() {
    super();
  }

  /**
   * Connect this data source to the table. The table will only update when
   * the returned stream emits new items.
   * @returns A stream of the items to be rendered.
   */
  connect(): Observable<ActivityTableItem[]> {
    if (this.paginator && this.sort) {
      // Combine everything that affects the rendered data into one update
      // stream for the data-table to consume.
      return merge(observableOf(this.data), this.paginator.page, this.sort.sortChange)
        .pipe(map(() => {
          return this.getPagedData(this.getSortedData([...this.data ]));
        }));
    } else {
      throw Error('Please set the paginator and sort on the data source before connecting.');
    }
  }

  /**
   *  Called when the table is being destroyed. Use this function, to clean up
   * any open connections or free any held resources that were set up during connect.
   */
  disconnect(): void {}

  /**
   * Paginate the data (client-side). If you're using server-side pagination,
   * this would be replaced by requesting the appropriate data from the server.
   */
  private getPagedData(data: ActivityTableItem[]): ActivityTableItem[] {
    if (this.paginator) {
      const startIndex = this.paginator.pageIndex * this.paginator.pageSize;
      return data.splice(startIndex, this.paginator.pageSize);
    } else {
      return data;
    }
  }

  /**
   * Sort the data (client-side). If you're using server-side sorting,
   * this would be replaced by requesting the appropriate data from the server.
   */
  private getSortedData(data: ActivityTableItem[]): ActivityTableItem[] {
    if (!this.sort || !this.sort.active || this.sort.direction === '') {
      return data;
    }

    return data.sort((a, b) => {
      const isAsc = this.sort?.direction === 'asc';
      switch (this.sort?.active) {
        case 'title': return compare(a.title, b.title, isAsc);
        case 'get_leaders': return compare(+a.get_leaders, +b.get_leaders, isAsc);
        default: return 0;
      }
    });
  }
}

/** Simple sort comparator for example ID/Name columns (for client-side sorting). */
function compare(a: string | number, b: string | number, isAsc: boolean): number {
  return (a < b ? -1 : 1) * (isAsc ? 1 : -1);
}
