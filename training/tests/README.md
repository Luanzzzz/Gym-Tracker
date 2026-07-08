# Training test plan

The model tests are active and validate the current database implementation.

The view, CRUD, authentication, and search tests in `test_views.py` are marked
with `unittest.skip` because the matching views, URLs, and templates are planned
for the next phase. Remove the skip marker when implementing the CRUD backend.

Expected future URL namespace:

- `training:muscle-group-list`
- `training:muscle-group-detail`
- `training:muscle-group-create`
- `training:muscle-group-update`
- `training:muscle-group-delete`
- `training:exercise-list`
- `training:exercise-detail`
- `training:exercise-create`
- `training:exercise-update`
- `training:exercise-delete`
- `training:athlete-list`
- `training:athlete-detail`
- `training:workout-plan-list`
- `training:workout-plan-detail`
- `training:workout-plan-create`
- `training:workout-plan-update`
- `training:workout-plan-delete`
