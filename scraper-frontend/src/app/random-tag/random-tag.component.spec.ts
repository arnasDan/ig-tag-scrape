import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RandomTagComponent } from './random-tag.component';

describe('RandomTagComponent', () => {
  let component: RandomTagComponent;
  let fixture: ComponentFixture<RandomTagComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RandomTagComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RandomTagComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
  
});
