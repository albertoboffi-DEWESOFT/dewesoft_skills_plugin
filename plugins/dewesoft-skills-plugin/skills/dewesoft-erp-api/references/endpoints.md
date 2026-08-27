# Dewesoft ERP API — endpoint catalog (v1)

Source: apiDoc spec `api_data.js` (1,501 endpoints, 224 groups). All paths are relative to the regional base URL (IT = `https://erpapi-it-erp.dewesoft.com`). Every request needs `Authorization: Bearer <token>` except the OAuth2 login routes.

Machine-readable version with body-parameter details: `references/endpoints.json`. Most resources follow the universal six-route CRUD pattern documented in `references/conventions.md`.

## Groups

  AGVRobot · Activity_Event · Activity_Log · Addresses
  Announcements · Application · Archives · Attendance_Event
  Attendance_Event_Type · Attendance_Event_Type_Category · Attendance_MonthApproval · Attendance_Month_Approval
  Attendance_Request · Attendance_Requests · Attendance_event_type_categories · Attendance_event_types
  Attendance_events · Attendance_month_approval · Attendance_request · Bank_Account_Transactions
  Bank_Accounts · BatchSerials · Bom_Products · Bom_Types
  Boms · CachedData · Calibrator · Compensations
  Contacts · Cooperations · Cost_Centers · Countries
  Currency_Codes · Currency_Rates · Custom_Columns · Delivery_Note_Issued
  Delivery_Note_Issued_Items · Delivery_Note_Received · Delivery_Note_Received_Items · Delivery_note_issued
  Departments · Document_Types · Documents · Ds_License_Code_Types
  Ds_License_Codes · Ds_License_Versions · Ds_Licenses · Employment_contract
  Employment_contracts · Employment_type · Employment_types · EventAction
  Expense_Events · Export_Attendance · Export_BC_Attendance · Export_Business_trips
  Export_Kids_of_employees · Export_Overtime_Yearly · Export_Years_of_service · Export_custom_vacation_report
  Export_customer_salary · Export_lunch · ExternalProducts · ExternalPurchase
  ExternalPurchases · External_products · Facilities · Financial_statements
  Fixed_Assets · FreshDesk · Goods_Rebook_Items · Goods_Rebooks
  Goods_Receipt_Items · Goods_Receipts · Goods_Transfer_Items · Goods_Transfers
  Goods_Writeoff_Items · Goods_Writeoffs · Google_mail · HR_External
  Holidays · Hr_Approver · Hr_Department · Hr_approver
  Hr_approvers · Hr_department · Hr_departments · Import
  Incoterms · Individual_reward · Industries · Invoice_Clauses
  Invoice_Issued · Invoice_Issued_Items · Invoice_Received · Invoice_Received_Items
  Job_Applications · Lots · Material_Classifications · Media
  Movement_Types · Notes · Notification_Channels · Notification_Templates
  Notifications · OAuth2 · Open_Invoice_Issued_for_Partner · Options
  Order · Order_Consumable_Items · Order_Consumables · Order_Purchase_Items
  Order_Purchases · Order_Quote_Items · Order_Quotes · Order_Sale_Items
  Order_Sales · Packing_Boxes · Packing_List_Items · Packing_Lists
  Partner_Applications · Partner_types · Partners · Payment_Methods
  Payment_Terms · PerformanceReviews · Permissions · Price_Lists
  Price_Templates · PrintSigners · Printer · Processes
  ProductDocumentation · Product_Line_Product · Product_Lines · Product_Types
  Production · ProductionOperations · Products · Projects
  Queue · Regions · ResourceTypes · Resources
  RewardsAndBonuses · Roles · Sale_Types · SalesForecast
  SalesForecastAdjustments · SalesForecastAdjustmentss · SalesForecasts · Sales_forecast
  Sales_forecast_items · Scheduled_jobs · Serial_BOMs · Serial_Calibrations
  Serial_Fields · Serials · Service_Errors · Service_Externals
  Service_Internals · Shipping_Lists · Shipping_Methods · Single_piece_flow_models
  Skills · SolutionAreas · Solutions · States
  Statistic · Status_Categories · Statuses · Stock_Adjustment_Items
  Stock_Adjustments · Stock_Bids · Stock_Initial_Items · Stock_Initials
  Stock_Taking_Report_Items · Stock_Taking_Reports · Stock_Takings · Stock_Transactions
  Stocks · Support_Inquiries · Sync_Bank_Account_Transactions · Tags
  Tariff_Codes · Tasks · Tax_Rates · Technologies
  TemplateTypes · Templates · Timeline · UndoHistory
  Units · Upgrades · User_Filters · User_Hr_Profile_Work_Equipment
  User_Hr_Profile_Work_Position · User_Hr_Profiles · User_Work_Position · User_hr_profile
  User_hr_profile_work_equipment · User_hr_profile_work_position · User_hr_profile_work_positions · User_hr_profiles
  User_saldo_month · User_work_position · User_work_positions · Users
  Warehouse_Locations · Warehouses · WorkOrderItem_BOMs · Work_Equipment
  Work_Location · Work_Locations · Work_Order_BOMs · Work_Order_Items
  Work_Orders · Work_Orders_Items · Work_equipment · Work_location
  Work_locations · Work_position_Hr_department · Work_position_hr_department · Workflow


## AGVRobot
- `GET /v1/agv-robots` — Paginate agv robots.
- `GET /v1/agv-robots` — Fin agv robot by id
- `PATCH /v1/agv-robots` — Update Agv robot with given  id.
    - body: name ((required)), external_id ((required))
- `POST /v1/agv-robots` — Create Agv robot
    - body: name ((required)), external_id ((required))
- `GET /v1/agv-robots/all` — Find all Agv robots
- `POST /v1/agv-robots/move-vehicle` — Move vehicle
- `GET /v1/agv-robots/vehicle-info` — Get AGV vehicle info
- `POST /v1/agv-robots/write-shared-memory` — Write shared memory
- `DELETE /v1/agv-robots/{id}` — Delete agv robot

## Activity_Event
- `GET /v1/activity-events-by-group` — Get activity events by group

## Activity_Log
- `POST /v1/activity-log` — Insert activity log
    - body: table ((required)), id ((required)), description ((required)), properties ((required)), user_id ((optional))
- `GET /v1/activity-log/:table/:id` — Get activity log

## Addresses
- `GET /v1/addresses` — Paginate Addresses
- `POST /v1/addresses` — Create Address
    - body: name ((required, max:255)), address1 ((optional, max:255)), address2 ((optional, max:255)), post ((optional, max:16)), city ((optional, max:255)), state_id ((optional, existsalpha:states.id, max:2)), country_id ((required, alpha, exists:countries.id, max:2)), latitude ((optional, max:20)), longitude ((optional, max:20)), phone ((optional, max:20)), mobile ((optional, max:20)), fax ((optional)), email ((optional)), primary ((optional)), is_eu ((optional)), calculate_vat ((optional)), addressable_id ((required, poly_exists:addressable_type)), addressable_type ((required)), is_billing ((optional)), is_shipping ((optional)), warehouse_location_id ((required, exists:warehouse_locations.id))
- `DELETE /v1/addresses/:id` — Delete Addresses
- `GET /v1/addresses/:id` — Get Addresses
- `PATCH /v1/addresses/:id` — Update Addresses
    - body: name ((required, max:255)), address1 ((optional, max:255)), address2 ((optional, max:255)), post ((optional, max:16)), city ((optional, max:255)), state_id ((optional, existsalpha:states.id, max:2)), country_id ((required, alpha, exists:countries.id, max:2)), latitude ((optional, max:20)), longitude ((optional, max:20)), phone ((optional, max:20)), mobile ((optional, max:20)), fax ((optional)), email ((optional)), primary ((optional)), is_eu ((optional)), calculate_vat ((optional)), addressable_id ((required, poly_exists:addressable_type)), addressable_type ((required)), is_billing ((optional)), is_shipping ((optional)), warehouse_location_id ((required, exists:warehouse_locations.id))
- `GET /v1/addresses/all` — Get all addresses
    - body: name ((required)), address1 ((optional)), address2 ((optional)), post ((optional)), city ((optional)), state_id ((optional)), country_id ((required)), latitude ((optional)), longitude ((optional)), phone ((optional)), mobile ((optional)), fax ((optional)), email ((optional)), primary ((optional)), addressable_id ((required)), addressable_type ((required))
- `GET /v1/addresses/get-address-by-string` — Get Address From String
    - body: query ((required))

## Announcements
- `GET /v1/announcements` — Paginate Announcements
- `GET /v1/announcements` — Paginate Announcements
- `GET /v1/announcements` — Paginate Announcements
- `POST /v1/announcements` — Create Announcement
    - body: user_id ((optional, exists:users.id)), role_id ((optional, exists:roles.id)), title ((required, required, max:255)), summary ((optional)), body ((optional)), date_from ((required, required, date)), date_through ((required, date)), commentable ((optional)), published ((optional)), ignore_on_new_category ((optional)), exposed ((optional)), notify ((optional)), translator_id ((optional)), custom_author ((optional)), show_internal ((optional)), show_external ((optional)), is_international ((optional))
- `GET /v1/announcements-dashboard` — Get_dashboard_announcements
- `DELETE /v1/announcements/:id` — Delete Announcements
- `GET /v1/announcements/:id` — Get Announcements
- `PATCH /v1/announcements/:id` — Update Announcements
    - body: user_id ((optional, exists:users.id)), role_id ((optional, exists:roles.id)), title ((required, required, max:255)), summary ((optional)), body ((optional)), date_from ((required, required, date)), date_through ((required, date)), commentable ((optional)), published ((optional)), ignore_on_new_category ((optional)), exposed ((optional)), notify ((optional)), translator_id ((optional)), custom_author ((optional)), show_internal ((optional)), show_external ((optional)), is_international ((optional))
- `PATCH /v1/announcements/:id` — Update Announcements
    - body: user_id ((optional, exists:users.id)), role_id ((optional, exists:roles.id)), title ((required, required, max:255)), summary ((optional)), body ((optional)), date_from ((required, required, date)), date_through ((required, date)), commentable ((optional)), published ((optional)), ignore_on_new_category ((optional)), exposed ((optional)), notify ((optional)), translator_id ((optional)), custom_author ((optional)), show_internal ((optional)), show_external ((optional)), is_international ((optional))
- `GET /v1/announcements/all` — Get All Announcements
- `GET /v1/announcements/getTodaysMenu` — GetTodaysMenu
- `GET /v1/announcements2` — Get Announcements With Categories

## Application
- `GET /download-export/` — Download export
- `PATCH /v1/attach-relation` — Attach relation
    - body: id ((required if ids are missing)), relation ((required)), value ((required)), table ((required if model is missing)<br>Example: &quot;users&quot;)
- `GET /v1/barcode-scanner` — Get object by barcode number
- `POST /v1/batch-delete` — Batch delete
    - body: model ((required if table is missing)<br>Example: &quot;User&quot; or &quot;App\Containers\User\Models\User&quot; if in different container), ids ((required)), table ((required if model is missing)<br>Example: &quot;users&quot;)
- `PATCH /v1/bulk-delete` — Bulk delete records
    - body: model ((required if table is missing)<br> Example: &quot;User&quot; or &quot;App\Containers\User\Models\User&quot; if in different container), ids ((required if id is missing)), table ((required if model is missing)<br>Example: &quot;users&quot;)
- `PATCH /v1/commands/custom-export` — Run custom export command
    - body: export ((required))
- `PATCH /v1/commands/run` — Run command
    - body: command ((required))
- `PATCH /v1/detach-relation` — Detach relation
    - body: id ((required if ids are missing)), relation ((required)), value ((required)), table ((required if model is missing)<br>Example: &quot;users&quot;)
- `POST /v1/dislike/:table/:id` — Disike record
- `POST /v1/dislike/:table/:id` — Like record
- `POST /v1/dislike/:table/:id` — Like record
- `GET /v1/external-notification/new-release` — API health
- `GET /v1/get-enum-fields/:table/:field` — Get enum fields
- `GET /v1/get-fields/:table/:field` — Get table columns
- `GET /v1/get-fields/:table/:field` — Get table columns
- `GET /v1/get-fields/:table/:field` — Get table columns
- `GET /v1/get-table-configuration` — Get table configuration
- `GET /v1/health` — API health
- `GET /v1/health` — API health
- `GET /v1/health` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/health` — API health
- `GET /v1/health` — API health
- `GET /v1/health` — API health
- `PATCH /v1/invoices-issued/send-open-invoices-mail` — Send open invoices mail
    - body: to ((required)), subject ((required)), content ((required)), partner_id ((required))
- `PATCH /v1/invoices-issued/send-overdue-invoices-mail` — Send overdue invoices mail
    - body: to ((required)), subject ((required)), content ((required)), partner_id ((required))
- `PATCH /v1/restore` — Restore object
    - body: model ((required if table is missing)<br>Example: &quot;User&quot; or &quot;App\Containers\User\Models\User&quot; if in different container), id ((required if ids are missing)), ids ((required if id is missing)), table ((required if model is missing)<br>Example: &quot;users&quot;)
- `PATCH /v1/send-generic-mail` — Send generic mail
    - body: to ((required)), cc ((optional)), bcc ((optional)), subject ((required)), content ((required))
- `PATCH /v1/send-statement-of-account-mail` — Send generic mail
    - body: to ((required)), cc ((optional)), bcc ((optional)), subject ((required)), content ((required))
- `PATCH /v1/snapshot` — snapshot
- `PATCH /v1/snapshot` — Update field
- `PATCH /v1/update-field` — Update field
    - body: model ((required if table is missing)<br>Example: &quot;User&quot; or &quot;App\Containers\User\Models\User&quot; if in different container), id ((required if ids are missing)), ids ((required if id is missing)), field ((required)), value ((required)), table ((required if model is missing)<br>Example: &quot;users&quot;)
- `PATCH /v1/update-field` — Update field
    - body: model ((required if table is missing)<br>Example: &quot;User&quot; or &quot;App\Containers\User\Models\User&quot; if in different container), id ((required if ids are missing)), ids ((required if id is missing)), field ((required)), value ((required)), table ((required if model is missing)<br>Example: &quot;users&quot;)
- `PATCH /v1/update-field` — Update field
    - body: model ((required if table is missing)<br>Example: &quot;User&quot; or &quot;App\Containers\User\Models\User&quot; if in different container), id ((required if ids are missing)), ids ((required if id is missing)), field ((required)), value ((required)), table ((required if model is missing)<br>Example: &quot;users&quot;)
- `PATCH /v1/update-field` — Update field
    - body: model ((required if table is missing)<br>Example: &quot;User&quot; or &quot;App\Containers\User\Models\User&quot; if in different container), id ((required if ids are missing)), ids ((required if id is missing)), field ((required)), value ((required)), table ((required if model is missing)<br>Example: &quot;users&quot;)
- `PATCH /v1/update-field` — Update field
    - body: model ((required if table is missing)<br>Example: &quot;User&quot; or &quot;App\Containers\User\Models\User&quot; if in different container), id ((required if ids are missing)), ids ((required if id is missing)), field ((required)), value ((required)), table ((required if model is missing)<br>Example: &quot;users&quot;)
- `PATCH /v1/update-sort` — Update sort
    - body: model ((required if table is missing)<br>Example: &quot;User&quot; or &quot;App\Containers\User\Models\User&quot; if in different container), id ((required if ids are missing)), ids ((required if id is missing)), field ((required)), value ((required)), table ((required if model is missing)<br>Example: &quot;users&quot;)

## Archives
- `GET /v1/archives` — Paginate Archives
- `POST /v1/archives` — Create Archive
    - body: name ((required, max:255)), description ((optional)), contact_first_name ((optional, max:50)), contact_last_name ((optional, max:50)), contact_email ((optional)), contact_phone ((optional, max:20)), date_document ((optional, format:Y-m-d H:i:s))
- `DELETE /v1/archives/:id` — Delete Archive
- `GET /v1/archives/:id` — Get Archive
- `PATCH /v1/archives/:id` — Update Archive
    - body: name ((required, max:255)), description ((optional)), contact_first_name ((optional, max:50)), contact_last_name ((optional, max:50)), contact_email ((optional)), contact_phone ((optional, max:20)), date_document ((optional, format:Y-m-d H:i:s))
- `GET /v1/archives/all` — Get All Archives

## Attendance_Event
- `GET /v1/attendance-events` — Lists All Attendance events
- `POST /v1/attendance-events` — Create Attendance Event
    - body: active ((required)), value ((required)), date ((required, max:255)), night_work_date ((optional)), attendance_request_id ((required, exists:attendance_requests.id)), attendance_event_type_id ((required, exists:attendance_event_types.id)), user_id ((required, exists:users.id)), substitution_request_id ((optional, exists:attendance_requests.id))
- `GET /v1/attendance-events/:id` — Get Attendance Events
- `PATCH /v1/attendance-events/:id` — Update Attendance Event
    - body: active ((required)), value ((required)), date ((required, max:255)), night_work_date ((optional)), attendance_request_id ((required, exists:attendance_requests.id)), attendance_event_type_id ((required, exists:attendance_event_types.id)), user_id ((required, exists:users.id)), substitution_request_id ((optional, exists:attendance_requests.id))
- `GET /v1/attendance-events/all` — Get all Attendance Event

## Attendance_Event_Type
- `GET /v1/attendance-event-types` — Lists All Attendance event types
- `POST /v1/attendance-event-types` — Create Attendance Event Type
    - body: name ((optional)), require_end ((optional)), available_multiple_days ((optional)), count_in_saldo ((optional)), has_data ((optional)), visible_to_employee ((optional)), visible_to_approver ((optional)), icon ((optional)), is_timestamp ((optional)), has_work_location_choice ((optional)), time_before_event ((optional)), is_description_required ((optional)), external_approval ((optional)), is_partial ((optional)), notify_on_create ((optional)), notify_lead_on_request ((optional)), attendance_event_type_category_id ((optional, exists:attendance_event_type_categories.id))
- `GET /v1/attendance-event-types/:id` — Get Attendance Event Types
- `PATCH /v1/attendance-event-types/:id` — Update Attendance Event Type
    - body: name ((optional)), require_end ((optional)), available_multiple_days ((optional)), count_in_saldo ((optional)), has_data ((optional)), visible_to_employee ((optional)), visible_to_approver ((optional)), icon ((optional)), is_timestamp ((optional)), has_work_location_choice ((optional)), time_before_event ((optional)), is_description_required ((optional)), external_approval ((optional)), is_partial ((optional)), notify_on_create ((optional)), notify_lead_on_request ((optional)), attendance_event_type_category_id ((optional, exists:attendance_event_type_categories.id))
- `GET /v1/attendance-event-types/all` — Get all Attendance Event type

## Attendance_Event_Type_Category
- `GET /v1/attendance-event-type-categories` — Lists All Attendance event type categories
- `POST /v1/attendance-event-type-categories` — Create Attendance Event Type Categories
    - body: name ((required))
- `GET /v1/attendance-event-type-categories/:id` — Get Attendance Event Type categories
- `PATCH /v1/attendance-event-type-categories/:id` — Update Attendance Event Type Category
    - body: name ((required))
- `GET /v1/attendance-event-type-categories/all` — Get all Attendance Event Type Category

## Attendance_MonthApproval
- `GET /v1/attendance-month-approvals` — Lists All Attendance month approvals

## Attendance_Month_Approval
- `POST /v1/attendance-month-approval` — Create Attendance Month Approval
    - body: month ((required)), saldo_to_overtime ((optional)), user_id ((required, exists:users.id)), saldo_correction_request_id ((optional, exists:attendance_requests.id))
- `POST /v1/attendance-month-approval/insert-bulk` — Insert Bulk Attendance Month Approval
    - body: month ((required)), saldo_to_overtime ((optional)), user_id ((required, exists:users.id)), saldo_correction_request_id ((optional, exists:attendance_requests.id))
- `GET /v1/attendance-month-approvals/:id` — Get Attendance Month Approval
- `GET /v1/attendance-month-approvals/all` — Get all Attendance Month Approvals

## Attendance_Request
- `PATCH /v1/attendance-requests/:id` — Update Attendance Request
    - body: description ((required)), from ((required)), to ((required)), value ((required)), is_approved ((required)), lead_id ((required, exists:users.id)), employee_id ((required, exists:users.id)), attendance_event_type_id ((required, exists:attendance_event_types.id)), attendance_certificate_id ((required, exists:attendance_certificates.id)), work_location_id ((optional, exists:work_locations.id))
- `PATCH /v1/attendance-requests/:id` — Update Attendance Request
    - body: description ((required)), from ((required)), to ((required)), value ((required)), is_approved ((required)), lead_id ((required, exists:users.id)), employee_id ((required, exists:users.id)), attendance_event_type_id ((required, exists:attendance_event_types.id)), attendance_certificate_id ((required, exists:attendance_certificates.id)), work_location_id ((optional, exists:work_locations.id))
- `GET /v1/attendance-requests/all` — Get all Attendance Requests

## Attendance_Requests
- `POST /v1/attendance-requests` — Create Attendance Request
    - body: description ((required)), from ((required)), to ((required)), value ((required)), is_approved ((required)), lead_id ((required, exists:users.id)), employee_id ((required, exists:users.id)), attendance_event_type_id ((required, exists:attendance_event_types.id)), attendance_certificate_id ((required, exists:attendance_certificates.id)), work_location_id ((optional, exists:work_locations.id))
- `DELETE /v1/attendance-requests/:id` — Delete attendance requests
- `GET /v1/attendance-requests/:id` — Get Attendance Requests

## Attendance_event_type_categories
- `DELETE /v1/attendance-event-type-category/:id` — Delete attendance event type categories

## Attendance_event_types
- `DELETE /v1/attendance-event-types/:id` — Delete attendance event types

## Attendance_events
- `DELETE /v1/attendance-events/:id` — Delete attendance events

## Attendance_month_approval
- `DELETE /v1/attendance-month-approvals/:id` — Delete attendance month approval

## Attendance_request
- `GET /v1/attendance-requests` — Lists All Attendance requests

## Bank_Account_Transactions
- `GET /v1/bank-account-transactions` — Paginate Bank Account Transactions
- `POST /v1/bank-account-transactions` — Create Bank Account Transaction
    - body: partner_id ((optional, exists:partners,id)), bank_account_id ((required, bank_accounts,id)), transaction_id ((optional)), amount_inflow ((optional)), amount_outflow ((optional)), bank_commission ((optional)), currency_rate ((required)), name ((required, max:255)), date_transaction ((required)), bank_transaction_source_id ((required, exists:bank_transaction_sources.id)), amount_inflow_total ((optional)), amount_outflow_total ((optional))
- `DELETE /v1/bank-account-transactions/:id` — Delete Bank Account Transaction
- `GET /v1/bank-account-transactions/:id` — Get Bank Account Transaction
- `PATCH /v1/bank-account-transactions/:id` — Update Bank Account Transaction
    - body: partner_id ((optional, exists:partners,id)), bank_account_id ((required, bank_accounts,id)), transaction_id ((optional)), amount_inflow ((optional)), amount_outflow ((optional)), bank_commission ((optional)), currency_rate ((required)), name ((required, max:255)), date_transaction ((required)), bank_transaction_source_id ((required, exists:bank_transaction_sources.id)), amount_inflow_total ((optional)), amount_outflow_total ((optional))
- `GET /v1/bank-account-transactions/all` — Get All Bank Account Transactions

## Bank_Accounts
- `GET /v1/bank-accounts` — Paginate Bank Accounts
- `POST /v1/bank-accounts` — Create Bank Account
    - body: bank_accountable_id ((required, poly_exists:bank_accountable_type)), bank_accountable_type ((required)), bank_id ((required, exists:partners.id)), currency_code_id ((optional, currency_codes.id)), name ((required, max:255)), account_number ((optional, max:255)), transactional ((optional)), saving ((optional)), primary ((optional))
- `DELETE /v1/bank-accounts/:id` — Delete Bank Account
- `GET /v1/bank-accounts/:id` — Get Bank Account
- `GET /v1/bank-accounts/:id` — Get Bank Account
- `PATCH /v1/bank-accounts/:id` — Update Bank Account
    - body: bank_accountable_id ((required, poly_exists:bank_accountable_type)), bank_accountable_type ((required)), bank_id ((required, exists:partners.id)), currency_code_id ((optional, currency_codes.id)), name ((required, max:255)), account_number ((optional, max:255)), transactional ((optional)), saving ((optional)), primary ((optional))
- `GET /v1/bank-accounts/all` — Get All Bank Accounts
- `GET /v1/bank-accounts/all` — Get All Bank Accounts

## BatchSerials
- `POST /v1/batch-serials` — Create batch Serials
    - body: serial_number ((required))

## Bom_Products
- `GET /v1/bom-products` — Paginate Bom products
- `POST /v1/bom-products` — Create Bom Product
    - body: name ((required)), product_id ((required, exists:products.id)), bom_id ((required, exists:bom.id)), quantity ((required)), include_in_description ((optional))
- `DELETE /v1/bom-products/:id` — Delete bom product
- `GET /v1/bom-products/:id` — Get Bom product
- `PATCH /v1/bom-products/:id` — Update Bom Product
    - body: name ((required)), product_id ((required, exists:products.id)), bom_id ((required, exists:bom.id)), quantity ((required)), include_in_description ((optional))
- `GET /v1/bom-products/all` — Get All Bom products
- `GET /v1/bom-technologies` — Paginate Bom technologies
- `POST /v1/bom-technologies` — Create Bom Product
    - body: technology_id ((required, exists:technologies.id)), bom_id ((required, exists:bom.id)), duration ((required)), assigned_user_id ((optional, exists:users.id)), assigned_resource_id ((optional, exists:resources.id)), sort_order ((optional)), startup_time ((optional))
- `DELETE /v1/bom-technologies/:id` — Delete bom technology
- `GET /v1/bom-technologies/:id` — Get Bom technology
- `PATCH /v1/bom-technologies/:id` — Update Bom Product
    - body: technology_id ((required, exists:technologies.id)), bom_id ((required, exists:bom.id)), duration ((required)), assigned_user_id ((optional, exists:users.id)), assigned_resource_id ((optional, exists:resources.id)), sort_order ((optional)), startup_time ((optional))
- `PATCH /v1/bom-technologies/:id/sync-work-order-item-technologies` — Sync work order technologies
    - body: work_order_item_technology_ids ((required))
- `GET /v1/bom-technologies/all` — Get All Bom technologies

## Bom_Types
- `GET /v1/bom-types` — Paginate Bom types
- `POST /v1/bom-types` — Create Bom Type
    - body: name ((required, max:255))
- `DELETE /v1/bom-types/:id` — Delete bom type
- `GET /v1/bom-types/:id` — Get Bom type
- `PATCH /v1/bom-types/:id` — Update Bom Type
    - body: name ((required, max:255))
- `GET /v1/bom-types/all` — Get All Bom types

## Boms
- `GET /v1/boms` — Paginate Boms
- `POST /v1/boms` — Create Bom
    - body: name ((required, max:255)), product_id ((required, exists:products.id)), bom_type_id ((required, exists:bom_types.id)), amount_material ((optional)), amount_labour ((optional)), active ((optional))
- `DELETE /v1/boms/:id` — Delete bom
- `GET /v1/boms/:id` — Get Bom
- `PATCH /v1/boms/:id` — Update Bom
    - body: name ((required, max:255)), product_id ((required, exists:products.id)), bom_type_id ((required, exists:bom_types.id)), amount_material ((optional)), amount_labour ((optional)), active ((optional))
- `POST /v1/boms/:id/duplicate` — Duplicate Bom
- `POST /v1/boms/:id/duplicate` — Duplicate Bom
- `GET /v1/boms/:id/get-available-build-quantity` — Get available build quantity
- `POST /v1/boms/:id/insert-bom-products` — Insert BOM products
    - body: from_bom_id ((required))
- `POST /v1/boms/:id/replace-bom-on-work-order-items` — Replace BOM on work orders
    - body: from_bom_id ((required))
- `GET /v1/boms/all` — Get Bom

## CachedData
- `GET /v1/cached-data/:key` — Get CachedData
- `POST /v1/cached-data/:key` — Set CachedData

## Calibrator
- `POST /v1/calibrator/calibrator1.{extension?}` — CCalibrator1
- `POST /v1/calibrator/calibrator2.{extension?}` — Calibrator2
- `POST /v1/calibrator/generate_production_serial` — GenerateProductionSerial
- `POST /v1/calibrator/system_builder_v2.{extension?}` — SystemBuilderV2

## Compensations
- `GET /v1/compensations` — Paginate Compensations
- `POST /v1/compensations` — Create Compensation
    - body: partner_id ((required, exists:partners.id)), name ((required, max:255)), description ((optional)), amount_inflow ((optional)), amount_outflow ((optional)), currency_rate ((required)), date_compensation ((optional, format:Y-m-d H:i:s))
- `DELETE /v1/compensations/:id` — Delete Compensation
- `GET /v1/compensations/:id` — Get compensation
- `PATCH /v1/compensations/:id` — Update Compensation
    - body: partner_id ((required, exists:partners.id)), name ((required, max:255)), description ((optional)), amount_inflow ((optional)), amount_outflow ((optional)), currency_rate ((required)), date_compensation ((optional, format:Y-m-d H:i:s))
- `GET /v1/compensations/all` — Get all compensations

## Contacts
- `GET /v1/contacts` — Lists All Contacts
- `POST /v1/contacts` — Create Contact
    - body: first_name ((required, max:255)), last_name ((required, max:255)), company ((optional, max:255)), email ((required, max:255)), phone ((optional, max:25)), country_id ((required, exists:countries,id)), support_type ((optional)), content ((optional))
- `DELETE /v1/contacts/:id` — Delete Contact
- `GET /v1/contacts/:id` — Get Contact
- `PATCH /v1/contacts/:id` — Update Contact
    - body: first_name ((required, max:255)), last_name ((required, max:255)), company ((optional, max:255)), email ((required, max:255)), phone ((optional, max:25)), country_id ((required, exists:countries,id)), support_type ((optional)), content ((optional))
- `GET /v1/contacts/all` — Get Contact

## Cooperations
- `GET /v1/cooperations` — Lists All Cooperations
- `GET /v1/cooperations` — Lists All Cooperations
- `GET /v1/cooperations` — Lists All Cooperations
- `POST /v1/cooperations` — Create Cooperation
    - body: slug ((required)), sales_forecast_id ((required, exists:sales_forecasts.id)), parent_id ((optional, exists:sales_forecast_items.id)), product_id ((optional, exists:products.id)), tag_id ((optional, exists:tags.id)), quantity ((optional)), quantity_rolling ((optional)), quantity_actual ((optional)), amount_total ((optional)), amount_total_rolling ((optional)), amount_total_actual ((optional))
- `POST /v1/cooperations` — Create Cooperation
    - body: slug ((required)), sales_forecast_id ((required, exists:sales_forecasts.id)), parent_id ((optional, exists:sales_forecast_items.id)), product_id ((optional, exists:products.id)), tag_id ((optional, exists:tags.id)), quantity ((optional)), quantity_rolling ((optional)), quantity_actual ((optional)), amount_total ((optional)), amount_total_rolling ((optional)), amount_total_actual ((optional))
- `POST /v1/cooperations` — Create Cooperation
    - body: slug ((required)), sales_forecast_id ((required, exists:sales_forecasts.id)), parent_id ((optional, exists:sales_forecast_items.id)), product_id ((optional, exists:products.id)), tag_id ((optional, exists:tags.id)), quantity ((optional)), quantity_rolling ((optional)), quantity_actual ((optional)), amount_total ((optional)), amount_total_rolling ((optional)), amount_total_actual ((optional))
- `POST /v1/cooperations` — Create Cooperation
    - body: slug ((required)), sales_forecast_id ((required, exists:sales_forecasts.id)), parent_id ((optional, exists:sales_forecast_items.id)), product_id ((optional, exists:products.id)), tag_id ((optional, exists:tags.id)), quantity ((optional)), quantity_rolling ((optional)), quantity_actual ((optional)), amount_total ((optional)), amount_total_rolling ((optional)), amount_total_actual ((optional))
- `POST /v1/cooperations` — Create Cooperation
    - body: slug ((required)), sales_forecast_id ((required, exists:sales_forecasts.id)), parent_id ((optional, exists:sales_forecast_items.id)), product_id ((optional, exists:products.id)), tag_id ((optional, exists:tags.id)), quantity ((optional)), quantity_rolling ((optional)), quantity_actual ((optional)), amount_total ((optional)), amount_total_rolling ((optional)), amount_total_actual ((optional))
- `POST /v1/cooperations` — Create Cooperation
    - body: slug ((required)), sales_forecast_id ((required, exists:sales_forecasts.id)), parent_id ((optional, exists:sales_forecast_items.id)), product_id ((optional, exists:products.id)), tag_id ((optional, exists:tags.id)), quantity ((optional)), quantity_rolling ((optional)), quantity_actual ((optional)), amount_total ((optional)), amount_total_rolling ((optional)), amount_total_actual ((optional))
- `POST /v1/cooperations` — Create Cooperation
    - body: slug ((required)), sales_forecast_id ((required, exists:sales_forecasts.id)), parent_id ((optional, exists:sales_forecast_items.id)), product_id ((optional, exists:products.id)), tag_id ((optional, exists:tags.id)), quantity ((optional)), quantity_rolling ((optional)), quantity_actual ((optional)), amount_total ((optional)), amount_total_rolling ((optional)), amount_total_actual ((optional))
- `POST /v1/cooperations` — Create Cooperation
    - body: slug ((required)), sales_forecast_id ((required, exists:sales_forecasts.id)), parent_id ((optional, exists:sales_forecast_items.id)), product_id ((optional, exists:products.id)), tag_id ((optional, exists:tags.id)), quantity ((optional)), quantity_rolling ((optional)), quantity_actual ((optional)), amount_total ((optional)), amount_total_rolling ((optional)), amount_total_actual ((optional))
- `POST /v1/cooperations` — Create Cooperation
    - body: slug ((required)), sales_forecast_id ((required, exists:sales_forecasts.id)), parent_id ((optional, exists:sales_forecast_items.id)), product_id ((optional, exists:products.id)), tag_id ((optional, exists:tags.id)), quantity ((optional)), quantity_rolling ((optional)), quantity_actual ((optional)), amount_total ((optional)), amount_total_rolling ((optional)), amount_total_actual ((optional))
- `DELETE /v1/cooperations/:id` — Delete Cooperation
- `DELETE /v1/cooperations/:id` — Delete Cooperation
- `DELETE /v1/cooperations/:id` — Delete Cooperation
- `GET /v1/cooperations/:id` — Get Cooperation
- `GET /v1/cooperations/:id` — Get Cooperation
- `GET /v1/cooperations/:id` — Get Cooperation
- `GET /v1/cooperations/:id` — Get Cooperation
- `GET /v1/cooperations/:id` — Get Cooperation
- `PATCH /v1/cooperations/:id` — Update Cooperation
    - body: slug ((required)), sales_forecast_id ((required, exists:sales_forecasts.id)), parent_id ((optional, exists:sales_forecast_items.id)), product_id ((optional, exists:products.id)), tag_id ((optional, exists:tags.id)), quantity ((optional)), quantity_rolling ((optional)), quantity_actual ((optional)), amount_total ((optional)), amount_total_rolling ((optional)), amount_total_actual ((optional))
- `PATCH /v1/cooperations/:id` — Update Cooperation
    - body: slug ((required)), sales_forecast_id ((required, exists:sales_forecasts.id)), parent_id ((optional, exists:sales_forecast_items.id)), product_id ((optional, exists:products.id)), tag_id ((optional, exists:tags.id)), quantity ((optional)), quantity_rolling ((optional)), quantity_actual ((optional)), amount_total ((optional)), amount_total_rolling ((optional)), amount_total_actual ((optional))
- `PATCH /v1/cooperations/:id` — Update Cooperation
    - body: slug ((required)), sales_forecast_id ((required, exists:sales_forecasts.id)), parent_id ((optional, exists:sales_forecast_items.id)), product_id ((optional, exists:products.id)), tag_id ((optional, exists:tags.id)), quantity ((optional)), quantity_rolling ((optional)), quantity_actual ((optional)), amount_total ((optional)), amount_total_rolling ((optional)), amount_total_actual ((optional))
- `PATCH /v1/cooperations/:id` — Update Cooperation
    - body: slug ((required)), sales_forecast_id ((required, exists:sales_forecasts.id)), parent_id ((optional, exists:sales_forecast_items.id)), product_id ((optional, exists:products.id)), tag_id ((optional, exists:tags.id)), quantity ((optional)), quantity_rolling ((optional)), quantity_actual ((optional)), amount_total ((optional)), amount_total_rolling ((optional)), amount_total_actual ((optional))
- `PATCH /v1/cooperations/:id` — Update Cooperation
    - body: slug ((required)), sales_forecast_id ((required, exists:sales_forecasts.id)), parent_id ((optional, exists:sales_forecast_items.id)), product_id ((optional, exists:products.id)), tag_id ((optional, exists:tags.id)), quantity ((optional)), quantity_rolling ((optional)), quantity_actual ((optional)), amount_total ((optional)), amount_total_rolling ((optional)), amount_total_actual ((optional))
- `GET /v1/cooperations/all` — Get all Cooperations
- `GET /v1/cooperations/all` — Get all Cooperations
- `GET /v1/cooperations/all` — Get all Cooperations

## Cost_Centers
- `GET /v1/cost-centers` — Index Cost Center
- `POST /v1/cost-centers` — Create Cost Center
    - body: parent_id ((optional, exists:cost_centers.id)), name ((required, max:255)), full_path_name ((optional)), description ((optional)), sort_order ((optional)), enabled ((required))
- `DELETE /v1/cost-centers/:id` — Delete Cost Center
- `GET /v1/cost-centers/:id` — Get Cost Center
- `PATCH /v1/cost-centers/:id` — Update Cost Center
    - body: parent_id ((optional, exists:cost_centers.id)), name ((required, max:255)), full_path_name ((optional)), description ((optional)), sort_order ((optional)), enabled ((required))
- `GET /v1/cost-centers/all` — Get Cost Center

## Countries
- `GET /v1/countries` — Paginate Countries
- `POST /v1/countries` — Create Sale Type
    - body: short_name ((required, max:255)), long_name ((required, max:255)), iso3 ((required, unique:countries, iso3, max:3, min:3)), alternative_code ((optional)), numcode ((required, max:3, min:3)), calling_code ((optional, max:20)), currency_code_id ((optional, exists:currency_codes.id, max:3)), cctld ((optional, max:20)), un_member ((required)), euc ((required)), sales_emails ((optional)), show_in_shop ((required)), require_euc_verification ((required)), end_customer_required ((required)), longitude ((optional)), latitude ((optional))
- `GET /v1/countries-public` — Index Countries public
- `GET /v1/countries-public/all` — Get all Countries public
- `DELETE /v1/countries/:id` — Delete Country
- `GET /v1/countries/:id` — Get Country
- `PATCH /v1/countries/:id` — Update Country
    - body: short_name ((required, max:255)), long_name ((required, max:255)), iso3 ((required, unique:countries, iso3, max:3, min:3)), alternative_code ((optional)), numcode ((required, max:3, min:3)), calling_code ((optional, max:20)), currency_code_id ((optional, exists:currency_codes.id, max:3)), cctld ((optional, max:20)), un_member ((required)), euc ((required)), sales_emails ((optional)), show_in_shop ((required)), require_euc_verification ((required)), end_customer_required ((required)), longitude ((optional)), latitude ((optional))
- `GET /v1/countries/all` — Get all Countries

## Currency_Codes
- `GET /v1/currency-codes` — Index Currency Codes
- `POST /v1/currency-codes` — Create Currency Code
    - body: id ((required, unique:currency_codes.id, alpha, max:3) Drugacen id?), name ((required, max:255)), symbol ((optional))
- `DELETE /v1/currency-codes/:id` — Delete Currency Code
- `GET /v1/currency-codes/:id` — Get Currency Codes
- `PATCH /v1/currency-codes/:id` — Update Currency Codes
    - body: id ((required, unique:currency_codes.id, alpha, max:3) Drugacen id?), name ((required, max:255)), symbol ((optional))
- `GET /v1/currency-codes/all` — Get Currency Codes
- `GET /v1/financial-statements` — Index Currency Codes
- `POST /v1/financial-statements` — Create Currency Code
    - body: name ((required)), partner_id ((required, exists:partners,id)), financial_statement_type_id ((required, exists:financial_statement_types.id)), country_id ((required, exists:countries.id)), currency_code_id ((required, exists:currency_codes.id)), month ((required, min:1, max:12)), year ((required, min:2000, max:2100)), currency_rate ((required))
- `DELETE /v1/financial-statements/:id` — Delete Currency Code
- `GET /v1/financial-statements/:id` — Get Currency Codes
- `PATCH /v1/financial-statements/:id` — Update Currency Codes
    - body: name ((required)), partner_id ((required, exists:partners,id)), financial_statement_type_id ((required, exists:financial_statement_types.id)), country_id ((required, exists:countries.id)), currency_code_id ((required, exists:currency_codes.id)), month ((required, min:1, max:12)), year ((required, min:2000, max:2100)), currency_rate ((required))
- `GET /v1/financial-statements/all` — Get Currency Codes

## Currency_Rates
- `GET /v1/currency-rates` — Paginate Currency Rates
- `POST /v1/currency-rates` — Create Currency Rate
    - body: currency_code_id ((required, alpha, exists:currency_codes.id)), rate ((required)), date_valid_from ((optional, format:Y-m-d H:i:s))
- `GET /v1/currency-rates/:date` — Get Currency Rates By Date
- `DELETE /v1/currency-rates/:id` — Delete Currency Rate
- `GET /v1/currency-rates/:id` — Get  Currency Rates
- `PATCH /v1/currency-rates/:id` — Update Currency Rates
    - body: currency_code_id ((required, alpha, exists:currency_codes.id)), rate ((required)), date_valid_from ((optional, format:Y-m-d H:i:s))
- `GET /v1/currency-rates/all` — Get  Currency Rates

## Custom_Columns
- `POST /v1/custom-columns` — Create Custom Column
- `POST /v1/custom-columns` — Create Custom Column
- `POST /v1/custom-columns` — Create Custom Column
- `POST /v1/custom-columns` — Create Custom Column
- `POST /v1/custom-columns` — Create Custom Column

## Delivery_Note_Issued
- `GET /v1/delivery-notes-issued` — Paginate Delivery Notes Issued
- `POST /v1/delivery-notes-issued Create Delivery Note` — Issued
    - body: shipping_list_id ((optional, exists:shipping_lists.id)), packing_list_id ((optional, exists:packing_lists.id)), invoice_received_id ((optional, exists:invoices_received.id)), user_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), document_type_id ((optional, exists:document_types.id)), document_number ((required)), reference_number ((required)), internal_reference_number ((required)), shipping_company ((optional, max:255)), shipping_address1 ((optional, max:255)), shipping_address2 ((optional, max:255)), shipping_post ((optional, max:16)), shipping_city ((optional, max:255)), shipping_country_id ((optional, max:2, exists:countries.id)), shipping_state_id ((optional, max:2, exists:states.id)), date_delivery ((optional, format:Y-m-d H:i:s)), date_received ((optional, format:Y-m-d H:i:s)), print_footer ((optional)), legal_notes ((optional))
- `POST /v1/delivery-notes-issued Create Delivery Note` — Issued
    - body: shipping_list_id ((optional, exists:shipping_lists.id)), packing_list_id ((optional, exists:packing_lists.id)), invoice_received_id ((optional, exists:invoices_received.id)), user_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), document_type_id ((optional, exists:document_types.id)), document_number ((required)), reference_number ((required)), internal_reference_number ((required)), shipping_company ((optional, max:255)), shipping_address1 ((optional, max:255)), shipping_address2 ((optional, max:255)), shipping_post ((optional, max:16)), shipping_city ((optional, max:255)), shipping_country_id ((optional, max:2, exists:countries.id)), shipping_state_id ((optional, max:2, exists:states.id)), date_delivery ((optional, format:Y-m-d H:i:s)), date_received ((optional, format:Y-m-d H:i:s)), print_footer ((optional)), legal_notes ((optional))
- `POST /v1/delivery-notes-issued Create Delivery Note` — Issued
    - body: shipping_list_id ((optional, exists:shipping_lists.id)), packing_list_id ((optional, exists:packing_lists.id)), invoice_received_id ((optional, exists:invoices_received.id)), user_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), document_type_id ((optional, exists:document_types.id)), document_number ((required)), reference_number ((required)), internal_reference_number ((required)), shipping_company ((optional, max:255)), shipping_address1 ((optional, max:255)), shipping_address2 ((optional, max:255)), shipping_post ((optional, max:16)), shipping_city ((optional, max:255)), shipping_country_id ((optional, max:2, exists:countries.id)), shipping_state_id ((optional, max:2, exists:states.id)), date_delivery ((optional, format:Y-m-d H:i:s)), date_received ((optional, format:Y-m-d H:i:s)), print_footer ((optional)), legal_notes ((optional))
- `DELETE /v1/delivery-notes-issued/:id` — Delete Delivery Note Issued
- `PATCH /v1/delivery-notes-issued/:id` — Update Delivery Note Issued
    - body: shipping_list_id ((optional, exists:shipping_lists.id)), packing_list_id ((optional, exists:packing_lists.id)), invoice_received_id ((optional, exists:invoices_received.id)), user_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), document_type_id ((optional, exists:document_types.id)), document_number ((required)), reference_number ((required)), internal_reference_number ((required)), shipping_company ((optional, max:255)), shipping_address1 ((optional, max:255)), shipping_address2 ((optional, max:255)), shipping_post ((optional, max:16)), shipping_city ((optional, max:255)), shipping_country_id ((optional, max:2, exists:countries.id)), shipping_state_id ((optional, max:2, exists:states.id)), date_delivery ((optional, format:Y-m-d H:i:s)), date_received ((optional, format:Y-m-d H:i:s)), print_footer ((optional)), legal_notes ((optional))
- `GET /v1/delivery-notes-issued/:id Get Delivery Note` — Issued
- `POST /v1/delivery-notes-issued/:id/send-mail` — Sen email delivery note issued
- `POST /v1/delivery-notes-issued/:id/send-mail` — Sen email delivery note issued
- `GET /v1/delivery-notes-issued/all` — Get Delivery Note Issued
- `POST /v1/delivery-notes-issued/{id}/invoice` — Create Invoice for Delivery note
    - body: partner_id ((required)), sale_type_id ((required)), date_payment ((required)), date_invoice ((required))
- `POST /v1/delivery-notes-issued/{id}/invoice` — Create Invoice for Delivery note
    - body: partner_id ((required)), sale_type_id ((required)), date_payment ((required)), date_invoice ((required))

## Delivery_Note_Issued_Items
- `GET /v1/delivery-note-issued-items` — Paginate Delivery Note Issued Items
- `PATCH /v1/delivery-note-issued-items Create Shipping` — Methods
    - body: delivery_note_issued_id ((required)), origin_country_id ((optional)), tariff_code_id ((optional)), product_id ((required)), saop_tax_rate_id ((optional)), unit_id ((optional)), sku ((required)), name ((required)), quantity ((required)), order_sale_item_id ((optional)), reference_number ((optional)), note ((optional))
- `DELETE /v1/delivery-note-issued-items/:id` — Delete Delivery Note Issued Items
- `GET /v1/delivery-note-issued-items/:id` — Get Delivery Note Issued Items
- `PATCH /v1/delivery-note-issued-items/:id` — Update Delivery Note Issued Items
    - body: delivery_note_issued_id ((required)), origin_country_id ((optional)), tariff_code_id ((optional)), product_id ((required)), saop_tax_rate_id ((optional)), unit_id ((optional)), sku ((required)), name ((required)), quantity ((required)), order_sale_item_id ((optional)), reference_number ((optional)), note ((optional))
- `GET /v1/delivery-note-issued-items/all` — Get Delivery Note Issued Items

## Delivery_Note_Received
- `GET /v1/delivery-notes-received` — Paginate Delivery Note Received
- `POST /v1/delivery-notes-received` — Create Delivery Note Received
    - body: invoice_received_id ((required, exists:invoices_received.id)), user_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), document_type_id ((required, exists:document_types.id)), document_number ((required)), shipping_company ((optional, max:255)), shipping_address1 ((optional, max:255)), shipping_address2 ((optional, max:255)), shipping_post ((optional, max:16)), shipping_city ((optional, max:255)), shipping_country_id ((optional, max:2, exists:countries.id)), shipping_state_id ((optional, max:2, exists:states.id)), date_delivery ((optional, format:Y-m-d H:i:s)), date_received ((optional, format:Y-m-d H:i:s)), date_notified ((optional, format:Y-m-d H:i:s))
- `DELETE /v1/delivery-notes-received/:id` — Delete Delivery Note Received
- `GET /v1/delivery-notes-received/:id` — Get Delivery Note Received
- `PATCH /v1/delivery-notes-received/:id` — Update Delivery Note Received
    - body: invoice_received_id ((required, exists:invoices_received.id)), user_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), document_type_id ((required, exists:document_types.id)), document_number ((required)), shipping_company ((optional, max:255)), shipping_address1 ((optional, max:255)), shipping_address2 ((optional, max:255)), shipping_post ((optional, max:16)), shipping_city ((optional, max:255)), shipping_country_id ((optional, max:2, exists:countries.id)), shipping_state_id ((optional, max:2, exists:states.id)), date_delivery ((optional, format:Y-m-d H:i:s)), date_received ((optional, format:Y-m-d H:i:s)), date_notified ((optional, format:Y-m-d H:i:s))
- `GET /v1/delivery-notes-received/all` — Get All Delivery Notes Received

## Delivery_Note_Received_Items
- `GET /v1/delivery-note-received-items` — Paginate Delivery Note Received Items
- `POST /v1/delivery-note-received-items` — Create Delivery Note Received Items
    - body: delivery_note_received_id ((required, exists:delivery_notes_received.id)), origin_country_id ((optional, sometimes, alpha, max:2, exists:countries.id)), tariff_code_id ((optional, exists:tariff_codes.id)), product_id ((required, exists:products.id)), unit_id ((optional, exists:units.id, max:5)), sku ((required, max:15)), name ((required, max:255)), quantity ((required)), note ((optional))
- `DELETE /v1/delivery-note-received-items/:id` — Delete Delivery Note Received Items
- `GET /v1/delivery-note-received-items/:id` — Get Delivery Note Received Items
- `PATCH /v1/delivery-note-received-items/:id` — Update Delivery Note Received Items
    - body: delivery_note_received_id ((required, exists:delivery_notes_received.id)), origin_country_id ((optional, sometimes, alpha, max:2, exists:countries.id)), tariff_code_id ((optional, exists:tariff_codes.id)), product_id ((required, exists:products.id)), unit_id ((optional, exists:units.id, max:5)), sku ((required, max:15)), name ((required, max:255)), quantity ((required)), note ((optional))
- `GET /v1/delivery-note-received-items/all` — Get All Delivery Note Received Items

## Delivery_note_issued
- `POST /v1/delivery-notes-issued/{id}/move-to-transit` — Move to transit
    - body: notify ((optional))

## Departments
- `GET /v1/departments` — Lists All Departments
- `POST /v1/departments` — Create Department
    - body: parent_id ((optional, exists:departments.id)), name ((required, max:255)), description ((optional)), sort_order ((optional)), is_strategy ((optional)), lead_user_id ((optional, exists:users.id)), matrix_lead_user_id ((optional, exists:users.id))
- `DELETE /v1/departments/:id` — Delete Department
- `GET /v1/departments/:id` — Get Department
- `PATCH /v1/departments/:id` — Update Department
    - body: parent_id ((optional, exists:departments.id)), name ((required, max:255)), description ((optional)), sort_order ((optional)), is_strategy ((optional)), lead_user_id ((optional, exists:users.id)), matrix_lead_user_id ((optional, exists:users.id))
- `GET /v1/departments/all` — Get all Departments

## Document_Types
- `GET /v1/document-types` — Lists All Document Types
- `POST /v1/document-types` — Create Document Type
    - body: document_id ((required, exists:documents.id)), name ((required, max:255)), description ((optional)), id_generator ((optional)), default ((optional)), numbering_date_field_name ((optional))
- `DELETE /v1/document-types/:id` — Delete Document Type
- `GET /v1/document-types/:id` — Get Document Types
- `PATCH /v1/document-types/:id` — Update Document Type
    - body: document_id ((required, exists:documents.id)), name ((required, max:255)), description ((optional)), id_generator ((optional)), default ((optional)), numbering_date_field_name ((optional))
- `GET /v1/document-types/all` — Get Document Types

## Documents
- `GET /v1/documents` — Lists All Documents
- `POST /v1/documents` — Create Document
    - body: table_name ((required, max:255)), name ((required, max:255)), description ((optional))
- `DELETE /v1/documents/:id` — Delete Document
- `GET /v1/documents/:id` — Get Document
- `GET /v1/documents/:id` — Get Document
- `PATCH /v1/documents/:id` — Update Document
    - body: table_name ((required, max:255)), name ((required, max:255)), description ((optional))
- `GET /v1/documents/all` — Get Document

## Ds_License_Code_Types
- `GET /v1/ds-license-code-types` — Paginate Ds License Code Types
- `POST /v1/ds-license-code-types` — Create Ds License Code Types
    - body: name ((required))
- `DELETE /v1/ds-license-code-types/:id` — Delete Ds License Code Types
- `GET /v1/ds-license-code-types/:id` — Get Ds License Code Types
- `PATCH /v1/ds-license-code-types/:id` — Update Ds License Code Types
    - body: name ((required))
- `GET /v1/ds-license-code-types/all` — Get all Ds License Code Types

## Ds_License_Codes
- `GET /v1/ds-license-codes` — Paginate Ds License Codes
- `POST /v1/ds-license-codes` — Create Ds License Codes
    - body: ds_license_code_type_id ((required, exists:ds_license_code_types.id)), ds_license_id ((required, exists:ds_licenses.id)), hw_key ((required)), hw_code ((required))
- `DELETE /v1/ds-license-codes/:id` — Delete Ds License Codes
- `GET /v1/ds-license-codes/:id` — Get Ds License Codes
- `PATCH /v1/ds-license-codes/:id` — Update Ds License Codes
    - body: ds_license_code_type_id ((required, exists:ds_license_code_types.id)), ds_license_id ((required, exists:ds_licenses.id)), hw_key ((required)), hw_code ((required))
- `GET /v1/ds-license-codes/all` — Get all Ds License Codes

## Ds_License_Versions
- `GET /v1/ds-license-versions` — Paginate Ds License Versions
- `POST /v1/ds-license-versions` — Create Ds License Versions
    - body: name ((required)), description ((optional)), version ((required))
- `DELETE /v1/ds-license-versions/:id` — Delete Ds License Versions
- `GET /v1/ds-license-versions/:id` — Get Ds License Versions
- `PATCH /v1/ds-license-versions/:id` — Update Ds License Versions
    - body: name ((required)), description ((optional)), version ((required))
- `GET /v1/ds-license-versions/all` — Get all Ds License Versions

## Ds_Licenses
- `GET /v1/ds-licenses` — Paginate Ds Licenses
- `GET /v1/ds-licenses` — Paginate Ds Licenses
- `POST /v1/ds-licenses` — Create Ds Licenses
    - body: order_sale_item_id ((optional, exists:order_sale_items.id)), product_id ((optional, exists:products.id)), ds_license_upgrade_from_id ((optional, exists:ds_licenses.id)), ds_license_upgrade_to_id ((optional, exists:ds_licenses.id)), ds_license_version_id ((optional, exists:ds_license_versions.id)), bundle ((optional)), require_registration ((optional)), key ((optional)), xml ((optional)), reg_count ((optional)), upgraded_at ((optional, format:Y-m-d H:i:s)), registered_at ((optional, format:Y-m-d H:i:s)), max_registrations ((optional)), expiration_in_months ((optional))
- `DELETE /v1/ds-licenses/:id` — Delete Ds Licenses
- `GET /v1/ds-licenses/:id` — Get Ds Licenses
- `PATCH /v1/ds-licenses/:id` — Update Ds Licenses
    - body: order_sale_item_id ((optional, exists:order_sale_items.id)), product_id ((optional, exists:products.id)), ds_license_upgrade_from_id ((optional, exists:ds_licenses.id)), ds_license_upgrade_to_id ((optional, exists:ds_licenses.id)), ds_license_version_id ((optional, exists:ds_license_versions.id)), bundle ((optional)), require_registration ((optional)), key ((optional)), xml ((optional)), reg_count ((optional)), upgraded_at ((optional, format:Y-m-d H:i:s)), registered_at ((optional, format:Y-m-d H:i:s)), max_registrations ((optional)), expiration_in_months ((optional))
- `PATCH /v1/ds-licenses/:id/reset` — Reset Ds Licenses
- `GET /v1/ds-licenses/all` — Get all Ds Licenses
- `POST /v1/ds-licenses/eval/request` — Request Eval Ds Licenses
    - body: order_sale_item_id ((optional, exists:order_sale_items.id)), product_id ((optional, exists:products.id)), ds_license_upgrade_from_id ((optional, exists:ds_licenses.id)), ds_license_upgrade_to_id ((optional, exists:ds_licenses.id)), ds_license_version_id ((optional, exists:ds_license_versions.id)), bundle ((optional)), require_registration ((optional)), key ((optional)), xml ((optional)), reg_count ((optional)), upgraded_at ((optional, format:Y-m-d H:i:s)), registered_at ((optional, format:Y-m-d H:i:s)), max_registrations ((optional)), expiration_in_months ((optional))

## Employment_contract
- `GET /v1/employment-contracts` — Lists All Employment contracts
- `PATCH /v1/employment-contracts/:id` — Update Employment contracts
    - body: name ((required))

## Employment_contracts
- `GET /v1/employment-contracts/:id` — Get Employment contracts

## Employment_type
- `GET /v1/employment-types` — Lists All Employment types
- `PATCH /v1/employment-types/:id` — Update Employment types
    - body: name ((required))

## Employment_types
- `GET /v1/employment-types/:id` — Get Employment types

## EventAction
- `GET /v1/event-actions` — Paginate EventAction
- `POST /v1/event-actions` — Create EventAction
    - body: name ((required, max:255)), event_full_class_name ((required)), action_full_class_name ((optional)), url ((optional)), http_method ((optional)), fail_on_error ((optional)), notify_on_error ((optional)), enabled ((optional)), args ((optional)), conditions (( optional))
- `DELETE /v1/event-actions/:id` — Delete EventAction
- `GET /v1/event-actions/:id` — Get event action
- `PATCH /v1/event-actions/:id` — Update EventAction
    - body: name ((required, max:255)), event_full_class_name ((required)), action_full_class_name ((optional)), url ((optional)), http_method ((optional)), fail_on_error ((optional)), notify_on_error ((optional)), enabled ((optional)), args ((optional)), conditions (( optional))
- `GET /v1/event-actions/all` — Get All EventAction

## Expense_Events
- `GET /v1/expense-events` — Lists All Expense Events
- `POST /v1/expense-events` — Create Expense Event
    - body: tax_rate_id ((required, exists:tax_rates.id)), name ((required, max:255)), konto_code ((required, max:20)), cost_type ((required, in:Fixed, Variable, Investment, Financing)), reward_system ((optional)), annual_calculation ((optional)), check_delivery ((optional)), check_delivery_add_tax ((optional)), konto_code_usage ((optional, max:20))
- `DELETE /v1/expense-events/:id` — Delete Expense Event
- `GET /v1/expense-events/:id` — Get Expense Events
- `PATCH /v1/expense-events/:id` — Update Expense Event
    - body: tax_rate_id ((required, exists:tax_rates.id)), name ((required, max:255)), konto_code ((required, max:20)), cost_type ((required, in:Fixed, Variable, Investment, Financing)), reward_system ((optional)), annual_calculation ((optional)), check_delivery ((optional)), check_delivery_add_tax ((optional)), konto_code_usage ((optional, max:20))
- `GET /v1/expense-events/all` — Get all Expense Events

## Export_Attendance
- `POST /v1/generate-export-attendance` — Create Export Attendance

## Export_BC_Attendance
- `POST /v1/generate-bc-export-attendance` — Create BC Export Attendance

## Export_Business_trips
- `POST /v1/generate-export-business-trips` — Create Export Business trips

## Export_Kids_of_employees
- `POST /v1/generate-export-kids-of-employees` — Create Export kids of employees

## Export_Overtime_Yearly
- `POST /v1/generate-export-overtime-yearly` — Create Overtime Yearly

## Export_Years_of_service
- `POST /v1/generate-export-years-of-service` — Create Export Years of service

## Export_custom_vacation_report
- `POST /v1/generate-custom-vacation-report` — Create custom vacation report

## Export_customer_salary
- `POST /v1/generate-custom-salary-export` — Create Export custom salary

## Export_lunch
- `POST /v1/generate-export-years-of-service` — Create Export lunch

## ExternalProducts
- `GET /v1/external-product` — Lists All ExternalProducts
- `GET /v1/external-product/:id` — Get External product

## ExternalPurchase
- `GET /v1/external-purchase/:id` — Get External Purchase

## ExternalPurchases
- `GET /v1/external-purchase` — Lists All ExternalPurchases

## External_products
- `PATCH /v1/external-products/update` — UpdateExternalProducts
    - body: ident ((optional)), ident_id ((optional)), material_name ((required, max:255)), mpn ((required, max:255)), qty_by_year_1 ((required, max:255)), qty_by_year_2 ((required, max:255)), qty_by_year_3 ((required, max:255)), price_min ((optional)), price_max ((optional)), stock_in_warehouse ((required, max:255)), demand_for_work_orders ((required, max:255))

## Facilities
- `GET /v1/facilities` — Paginate Facilities
- `POST /v1/facilities` — Create Facility
    - body: name ((required, max:255)), description ((optional)), is_production ((optional))
- `DELETE /v1/facilities/:id` — Delete Facility
- `GET /v1/facilities/:id` — Get Facility
- `PATCH /v1/facilities/:id` — Update Facility
    - body: name ((required, max:255)), description ((optional)), is_production ((optional))
- `GET /v1/facilities/all` — Get All Facilities

## Financial_statements
- `POST /v1/financial-statements/analyze-import-file` — Analyze import file financial statement
    - body: name ((required)), partner_id ((required, exists:partners,id)), financial_statement_type_id ((required, exists:financial_statement_types.id)), country_id ((required, exists:countries.id)), currency_code_id ((required, exists:currency_codes.id)), month ((required, min:1, max:12)), year ((required, min:2000, max:2100)), currency_rate ((required))
- `POST /v1/financial-statements/import-documents` — Import financial statements
    - body: name ((required)), partner_id ((required, exists:partners,id)), financial_statement_type_id ((required, exists:financial_statement_types.id)), country_id ((required, exists:countries.id)), currency_code_id ((required, exists:currency_codes.id)), month ((required, min:1, max:12)), year ((required, min:2000, max:2100)), currency_rate ((required))

## Fixed_Assets
- `GET /v1/fixed-assets` — Lists All Fixed Assets
- `POST /v1/fixed-assets` — Create Fixed Asset
    - body: serial_id ((required, exists:serials.id)), partner_id ((required, exists:partners.id)), invoice_received_id ((optional, exists:invoices_received.id)), name ((required, max:255)), description ((optional)), amount ((optional)), inventory_number ((required, max:255, unique:fixed_assets, inventory_number)), tracking_number ((optional, max:255)), trackable ((optional)), date_received ((optional, format:Y-m-d H:i:s)), date_activation ((optional, format:Y-m-d H:i:s)), date_liquidation ((optional, format:Y-m-d H:i:s))
- `DELETE /v1/fixed-assets/:id` — Delete Fixed Asset
- `GET /v1/fixed-assets/:id` — Get Fixed Assets
- `PATCH /v1/fixed-assets/:id` — Update Fixed Asset
    - body: serial_id ((required, exists:serials.id)), partner_id ((required, exists:partners.id)), invoice_received_id ((optional, exists:invoices_received.id)), name ((required, max:255)), description ((optional)), amount ((optional)), inventory_number ((required, max:255, unique:fixed_assets, inventory_number)), tracking_number ((optional, max:255)), trackable ((optional)), date_received ((optional, format:Y-m-d H:i:s)), date_activation ((optional, format:Y-m-d H:i:s)), date_liquidation ((optional, format:Y-m-d H:i:s))
- `GET /v1/fixed-assets/all` — Get all Fixed Assets
- `PATCH /v1/fixed-assets/tracking-info` — Update Fixed Asset tracking info
    - body: serial_id ((required, exists:serials.id)), partner_id ((required, exists:partners.id)), invoice_received_id ((optional, exists:invoices_received.id)), name ((required, max:255)), description ((optional)), amount ((optional)), inventory_number ((required, max:255, unique:fixed_assets, inventory_number)), tracking_number ((optional, max:255)), trackable ((optional)), date_received ((optional, format:Y-m-d H:i:s)), date_activation ((optional, format:Y-m-d H:i:s)), date_liquidation ((optional, format:Y-m-d H:i:s))

## FreshDesk
- `POST /v1/freshdesk/group/list` — Get list of freshdesk groups
- `POST /v1/freshdesk/ticket/new-from-comment` — Create New Ticket From Comment
- `POST /v1/note/parent/document-number` — Get Document Number

## Goods_Rebook_Items
- `GET /v1/goods-rebook-items` — Paginate Goods Rebook Items
- `POST /v1/goods-rebook-items` — Create Goods Rebook Items
    - body: goods_rebook_id ((required)), product_from_id ((required)), product_to_id ((required)), quantity ((required)), description ((optional))
- `DELETE /v1/goods-rebook-items/:id` — Delete Goods Rebook Items
- `GET /v1/goods-rebook-items/:id` — Get Goods Rebook Items
- `PATCH /v1/goods-rebook-items/:id` — Update Goods Rebook Items
    - body: goods_rebook_id ((required)), product_from_id ((required)), product_to_id ((required)), quantity ((required)), description ((optional))
- `GET /v1/goods-rebook-items/all` — Get Goods Rebook Items

## Goods_Rebooks
- `GET /v1/goods-rebooks` — List Goods Rebooks
- `POST /v1/goods-rebooks` — Create Goods Rebooks
    - body: movement_type_id ((required, in:401)), work_order_item_id ((optional, exists:work_order_items.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), description ((optional)), date_booked ((optional, format:Y-m-d H:i:s)), booked_by ((optional, exists:users.id)), date_closed ((optional, format:Y-m-d H:i:s)), closed_by ((optional, exists:users.id)), date_error ((optional, format:Y-m-d H:i:s)), error_description ((optional))
- `DELETE /v1/goods-rebooks/:id` — Delete Goods Rebooks
- `GET /v1/goods-rebooks/:id` — Get Goods Rebooks
- `PATCH /v1/goods-rebooks/:id` — Update Goods Rebooks
    - body: movement_type_id ((required, in:401)), work_order_item_id ((optional, exists:work_order_items.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), description ((optional)), date_booked ((optional, format:Y-m-d H:i:s)), booked_by ((optional, exists:users.id)), date_closed ((optional, format:Y-m-d H:i:s)), closed_by ((optional, exists:users.id)), date_error ((optional, format:Y-m-d H:i:s)), error_description ((optional))
- `GET /v1/goods-rebooks/:id/stock-transactions` — Get Goods Rebook stock transactions
- `GET /v1/goods-rebooks/all` — Get All Goods Rebooks

## Goods_Receipt_Items
- `GET /v1/goods-receipt-items` — Paginate Goods Receipt Items
- `POST /v1/goods-receipt-items` — Create Goods Receipt  Items
    - body: goods_receipt_id ((required, exists:goods_receipts.id)), invoice_received_id ((optional, exists:invoices_received.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), product_id ((required, exists:products.id)), origin_country_id ((optional, alpha, exists:countries.id)), order_purchase_item_id ((optional, exists:order_purchase_items.id)), order_sale_item_id ((optional, exists:order_sale_items.id)), quantity ((required) (optional)), quantity_counted ((required)), amount_currency ((optional)), amount_total_currency ((optional)), amount_costs_currency ((optional)), amount_costs_total_currency ((optional)), description ((optional)), weight_carton_total ((optional)), weight_plastic_total ((optional)), tariff_code_id ((optional, exists:tariff_codes.id)), document_type_id ((optional, exists:document_types.id)), document_number ((optional))
- `DELETE /v1/goods-receipt-items/:id` — Delete Goods Receipt  Items
- `PATCH /v1/goods-receipt-items/:id` — Update Goods Receipt  Items
    - body: goods_receipt_id ((required, exists:goods_receipts.id)), invoice_received_id ((optional, exists:invoices_received.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), product_id ((required, exists:products.id)), origin_country_id ((optional, alpha, exists:countries.id)), order_purchase_item_id ((optional, exists:order_purchase_items.id)), order_sale_item_id ((optional, exists:order_sale_items.id)), quantity ((required) (optional)), quantity_counted ((required)), amount_currency ((optional)), amount_total_currency ((optional)), amount_costs_currency ((optional)), amount_costs_total_currency ((optional)), description ((optional)), weight_carton_total ((optional)), weight_plastic_total ((optional)), tariff_code_id ((optional, exists:tariff_codes.id)), document_type_id ((optional, exists:document_types.id)), document_number ((optional))
- `PATCH /v1/goods-receipt-items/:id` — Update Goods Receipt  Items
    - body: goods_receipt_id ((required, exists:goods_receipts.id)), invoice_received_id ((optional, exists:invoices_received.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), product_id ((required, exists:products.id)), origin_country_id ((optional, alpha, exists:countries.id)), order_purchase_item_id ((optional, exists:order_purchase_items.id)), order_sale_item_id ((optional, exists:order_sale_items.id)), quantity ((required) (optional)), quantity_counted ((required)), amount_currency ((optional)), amount_total_currency ((optional)), amount_costs_currency ((optional)), amount_costs_total_currency ((optional)), description ((optional)), weight_carton_total ((optional)), weight_plastic_total ((optional)), tariff_code_id ((optional, exists:tariff_codes.id)), document_type_id ((optional, exists:document_types.id)), document_number ((optional))
- `PATCH /v1/goods-receipt-items/:id` — Update Goods Receipt  Items
    - body: goods_receipt_id ((required, exists:goods_receipts.id)), invoice_received_id ((optional, exists:invoices_received.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), product_id ((required, exists:products.id)), origin_country_id ((optional, alpha, exists:countries.id)), order_purchase_item_id ((optional, exists:order_purchase_items.id)), order_sale_item_id ((optional, exists:order_sale_items.id)), quantity ((required) (optional)), quantity_counted ((required)), amount_currency ((optional)), amount_total_currency ((optional)), amount_costs_currency ((optional)), amount_costs_total_currency ((optional)), description ((optional)), weight_carton_total ((optional)), weight_plastic_total ((optional)), tariff_code_id ((optional, exists:tariff_codes.id)), document_type_id ((optional, exists:document_types.id)), document_number ((optional))
- `GET /v1/goods-receipt-items/:id Get Goods` — Receipt Items
- `POST /v1/goods-receipt-items/:id/serials-multi` — Add multiple serials to goods receipt item
- `GET /v1/goods-receipt-items/all` — Get All Goods Receipt  Items

## Goods_Receipts
- `GET /v1/goods-receipts` — Paginate Goods Receipts
- `POST /v1/goods-receipts` — Create Goods Receipts
    - body: movement_type_id ((required, in:101, 102, 103, 104, 105, 106)), partner_id ((optional, exists:partners.id) //phpcs:ignore), order_purchase_id ((required_if:movement_type_id, 104, nullable, exists:orders_purchase.id)), order_sale_id ((required_if:movement_type_id, 106, nullable, exists:orders_sale.id)), work_order_item_id ((required_if:movement_type_id, 101, 102, 103, exists:work_order_items.id)), service_external_id ((required_if:movement_type_id, 105, exists:services_external.id)), upgrade_id ((required_if:movement_type_id, 105, exists:upgrades.id)), currency_code_id ((required, alpha, exists:currency_codes.id, max:3, min:3)), currency_rate ((required)), document_type_id ((optional, exists:document_types.id)), document_number ((optional, max:255)), partner_document_number ((optional, max:255)), amount_costs_currency ((optional)), cost_calculation_type ((optional, in:Even, Proportional)), date_document ((optional)), date_received ((optional)), date_booked ((optional, format:Y-m-d H:i:s)), booked_by ((optional, exists:users,id)), date_closed ((optional, format:Y-m-d H:i:s)), closed_by ((optional, exists:users,id)), date_error ((optional, format:Y-m-d H:i:s)), error_description ((optional))
- `POST /v1/goods-receipts` — Create Goods Receipts
    - body: movement_type_id ((required, in:101, 102, 103, 104, 105, 106)), partner_id ((optional, exists:partners.id) //phpcs:ignore), order_purchase_id ((required_if:movement_type_id, 104, nullable, exists:orders_purchase.id)), order_sale_id ((required_if:movement_type_id, 106, nullable, exists:orders_sale.id)), work_order_item_id ((required_if:movement_type_id, 101, 102, 103, exists:work_order_items.id)), service_external_id ((required_if:movement_type_id, 105, exists:services_external.id)), upgrade_id ((required_if:movement_type_id, 105, exists:upgrades.id)), currency_code_id ((required, alpha, exists:currency_codes.id, max:3, min:3)), currency_rate ((required)), document_type_id ((optional, exists:document_types.id)), document_number ((optional, max:255)), partner_document_number ((optional, max:255)), amount_costs_currency ((optional)), cost_calculation_type ((optional, in:Even, Proportional)), date_document ((optional)), date_received ((optional)), date_booked ((optional, format:Y-m-d H:i:s)), booked_by ((optional, exists:users,id)), date_closed ((optional, format:Y-m-d H:i:s)), closed_by ((optional, exists:users,id)), date_error ((optional, format:Y-m-d H:i:s)), error_description ((optional))
- `DELETE /v1/goods-receipts/:id` — Delete Goods Receipts
- `GET /v1/goods-receipts/:id` — Get Goods Receipts
- `PATCH /v1/goods-receipts/:id` — Update Goods Receipts
    - body: movement_type_id ((required, in:101, 102, 103, 104, 105, 106)), partner_id ((optional, exists:partners.id) //phpcs:ignore), order_purchase_id ((required_if:movement_type_id, 104, nullable, exists:orders_purchase.id)), order_sale_id ((required_if:movement_type_id, 106, nullable, exists:orders_sale.id)), work_order_item_id ((required_if:movement_type_id, 101, 102, 103, exists:work_order_items.id)), service_external_id ((required_if:movement_type_id, 105, exists:services_external.id)), upgrade_id ((required_if:movement_type_id, 105, exists:upgrades.id)), currency_code_id ((required, alpha, exists:currency_codes.id, max:3, min:3)), currency_rate ((required)), document_type_id ((optional, exists:document_types.id)), document_number ((optional, max:255)), partner_document_number ((optional, max:255)), amount_costs_currency ((optional)), cost_calculation_type ((optional, in:Even, Proportional)), date_document ((optional)), date_received ((optional)), date_booked ((optional, format:Y-m-d H:i:s)), booked_by ((optional, exists:users,id)), date_closed ((optional, format:Y-m-d H:i:s)), closed_by ((optional, exists:users,id)), date_error ((optional, format:Y-m-d H:i:s)), error_description ((optional))
- `GET /v1/goods-receipts/:id/book-to-stock` — Book Goods Receipts to stock
- `GET /v1/goods-receipts/:id/cancel` — Cancel Goods Receipts
- `GET /v1/goods-receipts/:id/stock-transactions` — Get Goods Receipt stock transactions
- `GET /v1/goods-receipts/all` — Get All Goods Receipts

## Goods_Transfer_Items
- `GET /v1/goods-transfer-items` — Paginate Goods Transfer Items
- `POST /v1/goods-transfer-items` — Create Goods Transfer Items
    - body: goods_transfer_id ((required, exists:goods_transfers.id)), warehouse_location_from_id ((optional, exists:warehouse_locations.id)), warehouse_location_to_id ((optional, exists:warehouse_locations.id)), product_id ((required, exists:products.id)), quantity ((required)), description ((optional))
- `DELETE /v1/goods-transfer-items/:id` — Delete Goods Transfer Items
- `GET /v1/goods-transfer-items/:id` — Get Goods Transfer Items
- `PATCH /v1/goods-transfer-items/:id` — Update Goods Transfer Items
    - body: goods_transfer_id ((required, exists:goods_transfers.id)), warehouse_location_from_id ((optional, exists:warehouse_locations.id)), warehouse_location_to_id ((optional, exists:warehouse_locations.id)), product_id ((required, exists:products.id)), quantity ((required)), description ((optional))
- `GET /v1/goods-transfer-items/all` — Get All Goods Transfer Items

## Goods_Transfers
- `GET /v1/goods-transfers` — Paginate Goods Transfers
- `POST /v1/goods-transfers` — Create Goods Transfers
    - body: movement_type_id ((optional, in:301, 302, 303, 304')), work_order_item_id ((optional, exists:work_order_items.id, required_if:movement_type_id, 302, 303, 304)), document_type_id ((optional, exists:document_types.id)), document_number ((optional, max:255)), description ((optional)), date_booked ((optional, format:Y-m-d H:i:s)), booked_by ((optional, exists:users.id)), date_error ((optional, format:Y-m-d H:i:s)), error_description ((optional)), order_consumable_id ((optional, exists:orders_consumable.id)), cooperation_id ((optional, exists:cooperations.id))
- `DELETE /v1/goods-transfers/:id` — Delete Goods Transfers
- `GET /v1/goods-transfers/:id` — Get Goods Transfers
- `PATCH /v1/goods-transfers/:id` — Update Goods Transfers
    - body: movement_type_id ((optional, in:301, 302, 303, 304')), work_order_item_id ((optional, exists:work_order_items.id, required_if:movement_type_id, 302, 303, 304)), document_type_id ((optional, exists:document_types.id)), document_number ((optional, max:255)), description ((optional)), date_booked ((optional, format:Y-m-d H:i:s)), booked_by ((optional, exists:users.id)), date_error ((optional, format:Y-m-d H:i:s)), error_description ((optional)), order_consumable_id ((optional, exists:orders_consumable.id)), cooperation_id ((optional, exists:cooperations.id))
- `GET /v1/goods-transfers/:id/book` — Book Goods Transfers
- `GET /v1/goods-transfers/:id/cancel` — Cancel Goods Transfers
- `GET /v1/goods-transfers/:id/stock-transactions` — Get Goods Transfer stock transactions
- `GET /v1/goods-transfers/all` — Get All Goods Transfers
- `POST /v1/goods-transfers/move-material-transfer` — Move material on work order item
    - body: movement_type_id ((optional, in:301, 302, 303, 304')), work_order_item_id ((optional, exists:work_order_items.id, required_if:movement_type_id, 302, 303, 304)), document_type_id ((optional, exists:document_types.id)), document_number ((optional, max:255)), description ((optional)), date_booked ((optional, format:Y-m-d H:i:s)), booked_by ((optional, exists:users.id)), date_error ((optional, format:Y-m-d H:i:s)), error_description ((optional)), order_consumable_id ((optional, exists:orders_consumable.id)), cooperation_id ((optional, exists:cooperations.id))
- `POST /v1/goods-transfers/unreservation-transfer` — Create Unreservation Goods Transfers
    - body: movement_type_id ((optional, in:301, 302, 303, 304')), work_order_item_id ((optional, exists:work_order_items.id, required_if:movement_type_id, 302, 303, 304)), document_type_id ((optional, exists:document_types.id)), document_number ((optional, max:255)), description ((optional)), date_booked ((optional, format:Y-m-d H:i:s)), booked_by ((optional, exists:users.id)), date_error ((optional, format:Y-m-d H:i:s)), error_description ((optional)), order_consumable_id ((optional, exists:orders_consumable.id)), cooperation_id ((optional, exists:cooperations.id))

## Goods_Writeoff_Items
- `GET /v1/goods-writeoff-items` — Paginate Goods Writeoff  Items
- `POST /v1/goods-writeoff-items Create Goods` — Writeoff  Items
    - body: goods_writeoff_id ((required, exists:goods_writeoffs.id)), invoice_received_id ((optional, exists:invoices_received.id)), goods_receipt_item_id ((optional, exists:goods_receipt_items.id)), goods_transfer_item_id ((optional, exists:goods_transfer_items.id)), product_id ((required, exists:products.id)), origin_country_id ((alpha, exists:countries.id)), warehouse_location_id ((required, exists:warehouse_locations.id)), quantity ((required)), amount_currency ((optional)), amount_total_currency ((optional)), amount_costs_currency ((optional)), amount_costs_total_currency ((optional)), description ((optional)), tariff_code_id ({Integrer} (optional, exists:tariff_codes.id))
- `DELETE /v1/goods-writeoff-items/:id` — Delete Goods Writeoff  Items
- `GET /v1/goods-writeoff-items/:id` — Get Goods Writeoff  Items
- `PATCH /v1/goods-writeoff-items/:id` — Update Goods Writeoff  Items
    - body: goods_writeoff_id ((required, exists:goods_writeoffs.id)), invoice_received_id ((optional, exists:invoices_received.id)), goods_receipt_item_id ((optional, exists:goods_receipt_items.id)), goods_transfer_item_id ((optional, exists:goods_transfer_items.id)), product_id ((required, exists:products.id)), origin_country_id ((alpha, exists:countries.id)), warehouse_location_id ((required, exists:warehouse_locations.id)), quantity ((required)), amount_currency ((optional)), amount_total_currency ((optional)), amount_costs_currency ((optional)), amount_costs_total_currency ((optional)), description ((optional)), tariff_code_id ({Integrer} (optional, exists:tariff_codes.id))
- `GET /v1/goods-writeoff-items/all` — Get All Goods Writeoff  Items

## Goods_Writeoffs
- `GET /v1/goods-writeoffs` — Paginate Goods Writeoffs
- `POST /v1/goods-writeoffs` — Create Goods Writeoffs
    - body: movement_type_id ((required, in:201, 202, 203, 204, 205, 206, 207, 208')), work_order_item_id ((required_if:movement_type_id, 201, 202, 203, exists:work_order_items.id)), order_purchase_id ((required_if:movement_type_id, 104, exists:orders_purchase.id)), goods_receipt_id ((exists:goods_receipts.id)), service_external_id ((optional, exists:services_external.id)), upgrade_id ((optional, exists:upgrades.id)), document_type_id ((required, exists:document_types.id)), currency_code_id ((alpha, exists:currency_codes.id, max:3, min:3)), currency_rate ((optional)), document_number ((optional, max:255)), date_booked ((optional, format:Y-m-d H:i:s)), booked_by ((optional, exists:users.id)), date_closed ((optional, format:Y-m-d H:i:s)), closed_by ((optional, exists:users.id)), date_error ((optional, format:Y-m-d H:i:s)), error_description ((optional)), confirmed ((optional))
- `DELETE /v1/goods-writeoffs/:id` — Delete Goods Writeoffs
- `GET /v1/goods-writeoffs/:id` — Get Goods Writeoffs
- `PATCH /v1/goods-writeoffs/:id` — Update Goods Writeoffs
    - body: movement_type_id ((required, in:201, 202, 203, 204, 205, 206, 207, 208')), work_order_item_id ((required_if:movement_type_id, 201, 202, 203, exists:work_order_items.id)), order_purchase_id ((required_if:movement_type_id, 104, exists:orders_purchase.id)), goods_receipt_id ((exists:goods_receipts.id)), service_external_id ((optional, exists:services_external.id)), upgrade_id ((optional, exists:upgrades.id)), document_type_id ((required, exists:document_types.id)), currency_code_id ((alpha, exists:currency_codes.id, max:3, min:3)), currency_rate ((optional)), document_number ((optional, max:255)), date_booked ((optional, format:Y-m-d H:i:s)), booked_by ((optional, exists:users.id)), date_closed ((optional, format:Y-m-d H:i:s)), closed_by ((optional, exists:users.id)), date_error ((optional, format:Y-m-d H:i:s)), error_description ((optional)), confirmed ((optional))
- `PATCH /v1/goods-writeoffs/:id` — Update Goods Writeoffs
    - body: movement_type_id ((required, in:201, 202, 203, 204, 205, 206, 207, 208')), work_order_item_id ((required_if:movement_type_id, 201, 202, 203, exists:work_order_items.id)), order_purchase_id ((required_if:movement_type_id, 104, exists:orders_purchase.id)), goods_receipt_id ((exists:goods_receipts.id)), service_external_id ((optional, exists:services_external.id)), upgrade_id ((optional, exists:upgrades.id)), document_type_id ((required, exists:document_types.id)), currency_code_id ((alpha, exists:currency_codes.id, max:3, min:3)), currency_rate ((optional)), document_number ((optional, max:255)), date_booked ((optional, format:Y-m-d H:i:s)), booked_by ((optional, exists:users.id)), date_closed ((optional, format:Y-m-d H:i:s)), closed_by ((optional, exists:users.id)), date_error ((optional, format:Y-m-d H:i:s)), error_description ((optional)), confirmed ((optional))
- `GET /v1/goods-writeoffs/:id/cancel` — Cancel Goods Writeoffs
- `GET /v1/goods-writeoffs/:id/stock-transactions` — Get Goods Writeoff stock transactions
- `GET /v1/goods-writeoffs/all` — Get All Goods Writeoffs

## Google_mail
- `GET /v1/google-mail-messages` — Google_mail_messages
- `GET /v1/google-mail-messages/{id}` — Google_mail_message_by_id
- `GET /v1/reply-to-google-mail-message` — Google_mail_message_reply

## HR_External
- `POST /v1/hr-external/post-approve-business-trip` — Post Approve Process For Business Trip
- `POST /v1/hr-external/post-finish-business-trip` — Post Finish Process For Business Trip

## Holidays
- `GET /v1/holidays` — Lists All Holidays
- `POST /v1/holidays` — Create Holiday
    - body: name ((required, max:255)), date ((required))
- `GET /v1/holidays-of-year/{year}` — Get All Holidays Of Year
- `DELETE /v1/holidays/:id` — Delete Holiday
- `GET /v1/holidays/:id` — Get Holidays
- `PATCH /v1/holidays/:id` — Update Holiday
    - body: name ((required, max:255)), date ((required))
- `GET /v1/holidays/all` — Get All Holidays
- `POST /v1/holidays/create-for-year` — Create All Holidays For Year

## Hr_Approver
- `PATCH /v1/hr-approvers/:id` — Update Hr approver
    - body: from ((required)), to ((required)), hr_department_id ((required, exists:hr_departments.id)), user_id ((required, exists:users.id))
- `GET /v1/hr-approvers/all` — Get all Hr Approvers

## Hr_Department
- `PATCH /v1/hr-departments/:id` — Update Hr department
    - body: name ((required)), description ((required)), parent_department_id ((required, exists:hr_departments.id)), lead_id ((required, exists:users.id)), cost_center_id ((optional, exists:cost_centers.id))
- `GET /v1/hr-departments/all` — Get all Hr Departments

## Hr_approver
- `GET /v1/hr-approvers` — Lists All Hr dapprovers

## Hr_approvers
- `POST /v1/hr-approvers` — Create Hr approvers
    - body: from ((required)), to ((required)), hr_department_id ((required, exists:hr_departments.id)), user_id ((required, exists:users.id))
- `DELETE /v1/hr-approvers/:id` — Delete Hr Approver
- `GET /v1/hr-approvers/:id` — Get Hr approvers

## Hr_department
- `GET /v1/hr-departments` — Lists All Hr departments

## Hr_departments
- `DELETE /v1/hr-department/:id` — Delete Hr Department
- `POST /v1/hr-departments` — Create Hr departments
    - body: name ((required)), description ((required)), parent_department_id ((required, exists:hr_departments.id)), lead_id ((required, exists:users.id)), cost_center_id ((optional, exists:cost_centers.id))
- `GET /v1/hr-departments/:id` — Get Hr departments

## Import
- `POST /v1/imports` — AnalyzeImportFile
    - body: file (File)
- `POST /v1/imports/{table_name}` — executeImport
    - body: table_name (String), map (Array), rows (Array)

## Incoterms
- `GET /v1/incoterms` — Paginate Incoterms
- `POST /v1/incoterms` — Create  Incoterms
    - body: code ((required)), description ((required))
- `DELETE /v1/incoterms/:id` — Delete Incoterms
- `GET /v1/incoterms/:id` — Get Incoterms
- `PATCH /v1/incoterms/:id` — Update Incoterms
    - body: code ((required)), description ((required))
- `GET /v1/incoterms/all` — Get All Incoterms

## Individual_reward
- `POST /v1/individual-reward-data` — Gathers individual reward table data

## Industries
- `GET /v1/industries` — Lists All Industries
- `POST /v1/industries` — Create Industry
    - body: name ((required, max:255)), description ((optional))
- `DELETE /v1/industries/:id` — Delete Industry
- `GET /v1/industries/:id` — Get Industry
- `PATCH /v1/industries/:id` — Update Industry
    - body: name ((required, max:255)), description ((optional))
- `GET /v1/industries/all` — Get All Industries

## Invoice_Clauses
- `POST /v1/invoice-clauses` — Create Invoice Clauses
    - body: name ((required, max:255)), description ((optional)), has_vat ((required))
- `GET /v1/invoice-clauses/` — Lists All Invoice Clauses
- `DELETE /v1/invoice-clauses/:id` — Delete Invoice Clauses
- `GET /v1/invoice-clauses/:id` — Get Invoice Clauses
- `PATCH /v1/invoice-clauses/:id` — Update Invoice Clauses
    - body: name ((required, max:255)), description ((optional)), has_vat ((required))
- `GET /v1/invoice-clauses/all` — Get All Invoice Clauses
- `PATCH /v1/invoices-issued/:id` — Update Invoice Clauses
    - body: parent_id ((optional)), user_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), invoice_clause_id ((optional, exists:invoice_clauses.id)), sale_type_id ((optional, exists:sale_types.id)), document_type_id ((required)), document_number ((required)), reference_number ((optional)), internal_reference_number ((optional)), mrn_number ((optional)), booking_number ((optional)), amount_total_currency ((required)), Numeric (}  amount_tal_currency  (reqiired)), amount_total ((required)), amount_open ((required)), amount_shipping_currency ((required)), financing_rate ((required)), amount_packaging_currency ((optional)), amount_financing_currency ((required)), amount_vat_currency ((required)), currency_rate ((required)), currency_code_id ((optional)), purpose ((optional)), billing_company ((optional)), billing_address1 ((optional)), billing_address2 ((optional)), billing_post ((optional)), billing_city ((optional)), billing_state_id ((optional)), billing_country_id ((optional)), vatid ((optional)), date_booking ((optional)), date_invoice ((optional)), date_payment ((optional)), date_paid ((optional)), date_service ((optional)), print_footer ((optional)), export_declaration (Boolean), is_eu (Boolean), calculate_vat (Boolean), additional_text (String), selected_partner_address_id (Integer), tax_register_invoice_eor (String), tax_register_invoice_zoi (String), ceo_full_name (String), legal_notes (String)

## Invoice_Issued
- `GET /v1/invoices-issued` — Lists All Invoice Issued
- `POST /v1/invoices-issued` — Create Invoice Issued
    - body: parent_id ((optional)), user_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), invoice_clause_id ((optional, exists:invoice_clauses.id)), sale_type_id ((optional, exists:sale_types.id)), document_type_id ((required)), document_number ((required)), reference_number ((optional)), internal_reference_number ((optional)), mrn_number ((optional)), booking_number ((optional)), amount_total_currency ((required)), Numeric (}  amount_tal_currency  (reqiired)), amount_total ((required)), amount_open ((required)), amount_shipping_currency ((required)), financing_rate ((required)), amount_packaging_currency ((optional)), amount_financing_currency ((required)), amount_vat_currency ((required)), currency_rate ((required)), currency_code_id ((optional)), purpose ((optional)), billing_company ((optional)), billing_address1 ((optional)), billing_address2 ((optional)), billing_post ((optional)), billing_city ((optional)), billing_state_id ((optional)), billing_country_id ((optional)), vatid ((optional)), date_booking ((optional)), date_invoice ((optional)), date_payment ((optional)), date_paid ((optional)), date_service ((optional)), print_footer ((optional)), export_declaration (Boolean), is_eu (Boolean), calculate_vat (Boolean), additional_text (String), selected_partner_address_id (Integer), tax_register_invoice_eor (String), tax_register_invoice_zoi (String), ceo_full_name (String), legal_notes (String)
- `DELETE /v1/invoices-issued/:id` — Delete Invoice Issued
- `GET /v1/invoices-issued/:id` — Get Invoice Issued
- `POST /v1/invoices-issued/:id/send-mail` — Sen email invoice issued
- `POST /v1/invoices-issued/:id/send-to-einvoice-api` — Sen email invoice issued
- `POST /v1/invoices-issued/:id/send-to-furs` — Sen email invoice issued
- `POST /v1/invoices-issued/:id/sync-invoice-order` — Sync invoice issued with order sale
- `GET /v1/invoices-issued/all` — Get All Invoice Issued
    - body: order_sale_id ((required))

## Invoice_Issued_Items
- `GET /v1/invoice-issued-items` — Lists All Invoice Issued Items
- `POST /v1/invoice-issued-items` — Create Invoice Issued Items
    - body: parent_id ((optional, exists:invoice_issued_items.id)), invoice_issued_id ((required, exists:invoices_issued.id)), order_sale_item_id ((optional, exists:order_sale_items.id)), origin_country_id ((optional, sometimes, alpha, max:2, exists:countries.id)), tariff_code_id ((optional, exists:tariff_codes.id)), saop_tax_rate_id ((optional, exists:tax_rates.id)), product_id ((required, exists:products.id)), unit_id ((optional, exists:units.id, alpha, max:5)), sku ((required, max:15)), short_name ((required, max:255)), name ((required) (max:255)), reference_number ((optional)), quantity ((required)), amount ((required)), discount_rate ((required)), amount_discount ((required)), tax_rate ((required)), amount_vat ((required)), amount_total ((required)), date_delivery_expected ((optional, format:Y-m-d H:i:s)), date_delivery_actual ((optional, format:Y-m-d H:i:s)), note ((optional))
- `GET /v1/invoice-issued-items/:id` — Get Invoice Issued Items
- `PATCH /v1/invoice-issued-items/:id` — Update Invoice Issued Items
    - body: parent_id ((optional, exists:invoice_issued_items.id)), invoice_issued_id ((required, exists:invoices_issued.id)), order_sale_item_id ((optional, exists:order_sale_items.id)), origin_country_id ((optional, sometimes, alpha, max:2, exists:countries.id)), tariff_code_id ((optional, exists:tariff_codes.id)), saop_tax_rate_id ((optional, exists:tax_rates.id)), product_id ((required, exists:products.id)), unit_id ((optional, exists:units.id, alpha, max:5)), sku ((required, max:15)), short_name ((required, max:255)), name ((required) (max:255)), reference_number ((optional)), quantity ((required)), amount ((required)), discount_rate ((required)), amount_discount ((required)), tax_rate ((required)), amount_vat ((required)), amount_total ((required)), date_delivery_expected ((optional, format:Y-m-d H:i:s)), date_delivery_actual ((optional, format:Y-m-d H:i:s)), note ((optional))
- `DELETE /v1/invoice-issued-items/:id Delete Invoice` — Issued Items
- `GET /v1/invoice-issued-items/all` — Get All Invoice Issued Items

## Invoice_Received
- `POST /v1/invoices-received` — Create Invoice Received
    - body: parent_id ((optional, exists:invoices_received.id)), partner_id ((optional, integer|exists:partners.id)), document_type_id ((required, exists:document_types.id)), document_number ((required)), partner_document_number ((required)), reference_number ((optional,max:100)), booking_number ((optional, max:100)), amount_total_currency ((required)), amount_total ((required)), amount_open ((required)), currency_rate ((required)), currency_code_id ((optional, alpha, exists:currency_codes.id)), purpose ((required, max:100)), proforma ((required)), advance_payment ((required)), credit_note ((required)), credit_card ((required)), has_connected_goods_documents ((optional)), forecast ((required)), date_received ((optional)), date_booking ((optional)), date_invoice ((optional)), date_vat ((optional)), date_payment ((optional)), date_paid ((optional)), date_service ((optional)), exported_to_bank ((optional)), invoice_received_type_id ((optional, exists:invoice_received_types.id)), dvpayer_partner_i ((optional, exists:partners.id))
- `POST /v1/invoices-received` — Create Invoice Received
    - body: parent_id ((optional, exists:invoices_received.id)), partner_id ((optional, integer|exists:partners.id)), document_type_id ((required, exists:document_types.id)), document_number ((required)), partner_document_number ((required)), reference_number ((optional,max:100)), booking_number ((optional, max:100)), amount_total_currency ((required)), amount_total ((required)), amount_open ((required)), currency_rate ((required)), currency_code_id ((optional, alpha, exists:currency_codes.id)), purpose ((required, max:100)), proforma ((required)), advance_payment ((required)), credit_note ((required)), credit_card ((required)), has_connected_goods_documents ((optional)), forecast ((required)), date_received ((optional)), date_booking ((optional)), date_invoice ((optional)), date_vat ((optional)), date_payment ((optional)), date_paid ((optional)), date_service ((optional)), exported_to_bank ((optional)), invoice_received_type_id ((optional, exists:invoice_received_types.id)), dvpayer_partner_i ((optional, exists:partners.id))
- `GET /v1/invoices-received/` — Lists All Invoice Received
- `DELETE /v1/invoices-received/:id` — Delete Invoice Received
- `GET /v1/invoices-received/:id` — Get Invoice Received
- `PATCH /v1/invoices-received/:id` — Update Invoice Received
    - body: parent_id ((optional, exists:invoices_received.id)), partner_id ((optional, integer|exists:partners.id)), document_type_id ((required, exists:document_types.id)), document_number ((required)), partner_document_number ((required)), reference_number ((optional,max:100)), booking_number ((optional, max:100)), amount_total_currency ((required)), amount_total ((required)), amount_open ((required)), currency_rate ((required)), currency_code_id ((optional, alpha, exists:currency_codes.id)), purpose ((required, max:100)), proforma ((required)), advance_payment ((required)), credit_note ((required)), credit_card ((required)), has_connected_goods_documents ((optional)), forecast ((required)), date_received ((optional)), date_booking ((optional)), date_invoice ((optional)), date_vat ((optional)), date_payment ((optional)), date_paid ((optional)), date_service ((optional)), exported_to_bank ((optional)), invoice_received_type_id ((optional, exists:invoice_received_types.id)), dvpayer_partner_i ((optional, exists:partners.id))
- `GET /v1/invoices-received/:id/goods-receipts` — Get Goods receipt for invoice
- `GET /v1/invoices-received/:id/goods-receipts` — Get Goods receipt for invoice
- `GET /v1/invoices-received/all` — Get All Invoices Received
- `POST /v1/invoices-received/{id}/close` — Close Invoice Received
    - body: parent_id ((optional, exists:invoices_received.id)), partner_id ((optional, integer|exists:partners.id)), document_type_id ((required, exists:document_types.id)), document_number ((required)), partner_document_number ((required)), reference_number ((optional,max:100)), booking_number ((optional, max:100)), amount_total_currency ((required)), amount_total ((required)), amount_open ((required)), currency_rate ((required)), currency_code_id ((optional, alpha, exists:currency_codes.id)), purpose ((required, max:100)), proforma ((required)), advance_payment ((required)), credit_note ((required)), credit_card ((required)), has_connected_goods_documents ((optional)), forecast ((required)), date_received ((optional)), date_booking ((optional)), date_invoice ((optional)), date_vat ((optional)), date_payment ((optional)), date_paid ((optional)), date_service ((optional)), exported_to_bank ((optional)), invoice_received_type_id ((optional, exists:invoice_received_types.id)), dvpayer_partner_i ((optional, exists:partners.id))

## Invoice_Received_Items
- `GET /v1/invoice-received-items` — Lists All Invoice Received Items
- `POST /v1/invoice-received-items` — Create Invoice Received Item
    - body: invoice_received_id ((required)), expense_event_id ((optional)), sku ((optional)), name ((required)), inventory_number ((optional)), quantity ((required)), amount ((required)), discount_rate ((required)), amount_discount ((required)), tax_rate ((required)), amount_vat ((required)), amount_total ((required))
- `DELETE /v1/invoice-received-items/:id` — Delete Invoice Received Item
- `GET /v1/invoice-received-items/:id` — Get Invoice Received Items
- `PATCH /v1/invoice-received-items/:id` — Update Invoice Received Items
    - body: invoice_received_id ((required)), expense_event_id ((optional)), sku ((optional)), name ((required)), inventory_number ((optional)), quantity ((required)), amount ((required)), discount_rate ((required)), amount_discount ((required)), tax_rate ((required)), amount_vat ((required)), amount_total ((required))
- `GET /v1/invoice-received-items/all` — Get All Invoice Received Items

## Job_Applications
- `GET /v1/job-applications` — Index Job Application
- `POST /v1/job-applications` — Create Job Application
    - body: type ((required, max:255)), position ((optional, max:255)), employment_type ((required, max:255)), find_about_us ((optional, max:255)), desired_position ((optional, max:255)), first_name ((optional, max:255)), last_name ((optional, max:255)), email ((optional, max:255)), phone ((optional, max:255)), country_id ((required, alpha, exists:countries.id)), city ((optional, max:255)), address ((optional, max:255)), post ((optional, max:255)), education ((optional, max:255)), msg ((optional)), cv_file ((optional, max:255)), school_report ((optional, max:255)), pdf_job_application ((optional, max:255)), responded ((optional)), date_responded ((optional)), invited ((optional,)), date_invited ((optional)), date_employment ((optional)), comment ((optional, max:255))
- `DELETE /v1/job-applications/:id` — Delete Job Application
- `GET /v1/job-applications/:id` — Get Job Application
- `PATCH /v1/job-applications/:id` — Update Job Application
    - body: type ((required, max:255)), position ((optional, max:255)), employment_type ((required, max:255)), find_about_us ((optional, max:255)), desired_position ((optional, max:255)), first_name ((optional, max:255)), last_name ((optional, max:255)), email ((optional, max:255)), phone ((optional, max:255)), country_id ((required, alpha, exists:countries.id)), city ((optional, max:255)), address ((optional, max:255)), post ((optional, max:255)), education ((optional, max:255)), msg ((optional)), cv_file ((optional, max:255)), school_report ((optional, max:255)), pdf_job_application ((optional, max:255)), responded ((optional)), date_responded ((optional)), invited ((optional,)), date_invited ((optional)), date_employment ((optional)), comment ((optional, max:255))
- `GET /v1/job-applications/all` — Get Job Application

## Lots
- `GET /v1/lots` — Lists All Lots
- `POST /v1/lots` — Create Lot
    - body: lot_id ((required)), product_id ((required, exists:products.id)), partner_id ((required, exists:partners.id)), origin_country_id ((optional, exists:countries.id)), amount ((required)), amount_material ((optional)), amount_material_net ((optional)), amount_labour ((optional)), amount_currency ((optional)), amount_costs ((optional))
- `DELETE /v1/lots/:id` — Delete Lot
- `GET /v1/lots/:id` — Get Lot
- `PATCH /v1/lots/:id` — Update Lot
    - body: lot_id ((required)), product_id ((required, exists:products.id)), partner_id ((required, exists:partners.id)), origin_country_id ((optional, exists:countries.id)), amount ((required)), amount_material ((optional)), amount_material_net ((optional)), amount_labour ((optional)), amount_currency ((optional)), amount_costs ((optional))
- `GET /v1/lots/:id/stock-transactions` — Get Lot stock transactions
- `GET /v1/lots/all` — Get All Lots

## Material_Classifications
- `GET /v1/export-control-classification-numbers` — Paginate Material Classifications
- `POST /v1/export-control-classification-numbers` — Create Material Classifications
    - body: code ((required, max:255)), name ((required, max:255)), description ((optional))
- `DELETE /v1/export-control-classification-numbers/:id` — Delete Material Classifications
- `GET /v1/export-control-classification-numbers/:id` — Get Material Classifications
- `PATCH /v1/export-control-classification-numbers/:id` — Update Material Classifications
    - body: code ((required, max:255)), name ((required, max:255)), description ((optional))
- `GET /v1/export-control-classification-numbers/all` — Get All Material Classifications
- `GET /v1/product-classifications` — Paginate Material Classifications
- `POST /v1/product-classifications` — Create Material Classifications
    - body: code ((required, alpha)), name ((required, max:255)), description ((optional)), has_serial ((optional)), depreciation_rate ((optional)), exclude_from_packing_list ((optional))
- `DELETE /v1/product-classifications/:id` — Delete Material Classifications
- `GET /v1/product-classifications/:id` — Get Material Classifications
- `PATCH /v1/product-classifications/:id` — Update Material Classifications
    - body: code ((required, alpha)), name ((required, max:255)), description ((optional)), has_serial ((optional)), depreciation_rate ((optional)), exclude_from_packing_list ((optional))
- `GET /v1/product-classifications/all` — Get All Material Classifications

## Media
- `POST /v1/media` — Create Media
    - body: file ((required)), model ((required)), model_id ((required))
- `DELETE /v1/media/:id` — Delete Media
    - body: id ((required))
- `GET /v1/media/:id` — Get Media
- `PATCH /v1/media/:id` — Update Media
    - body: name ((optional))
- `GET /v1/media/:id/download` — Download Media
    - body: id ((required))
- `GET /v1/media/:id/preview` — Preview Media
    - body: id ((required))
- `POST /v1/media/bulk` — Create Media in bulk
    - body: file ((required)), model ((required)), model_ids ((required))
- `POST /v1/media/copy` — Copy Media
    - body: copy_to_id ((required)), copy_from_id ((required)), copy_to_model ((required)), copy_from_model ((required)), delete_source_files ((required))
- `POST /v1/media/copy-bacth` — Copy Media
    - body: id_pairs ((required)), model_type ((required)), delete_source_files ((required))
- `GET /v1/media/download` — Download Zipped Media
- `GET /v1/media/{model}/{model_id}` — Get all Medias of a model
- `GET /v1/media/{model}/{model_id}` — Get all Medias of a model

## Movement_Types
- `GET /v1/stock-transactions/:document` — Get Movement types by Document
- `GET /v1/stock-transactions/all` — Get All Movement types

## Notes
- `GET /v1/notes` — Paginate Notes
- `POST /v1/notes` — Create note
    - body: parent_id ((optional, exists:notes.id)), content ((required)), public ((required)), notable_id ((required, poly_exists:notable_type)), notable_type ((required))
- `DELETE /v1/notes/:id` — Delete Note
- `GET /v1/notes/:id` — Get Note
- `PUT /v1/notes/:id` — Update note
    - body: parent_id ((optional, exists:notes.id)), content ((required)), public ((required)), notable_id ((required, poly_exists:notable_type)), notable_type ((required))
- `GET /v1/notes/all` — Get All Notes

## Notification_Channels
- `POST /v1/notification-channels Create Notification` — Channel
    - body: title ((required)), description ((required)), html ((required)), mjml ((required))
- `GET /v1/notification-channels/ Paginate Notification` — channels
- `DELETE /v1/notification-channels/:id Delete` — Notification Channel
- `GET /v1/notification-channels/:id Get Notification` — Channel
- `PATCH /v1/notification-channels/:id Update` — Notification Channel
    - body: title ((required)), description ((required)), html ((required)), mjml ((required)), notificationchannel.description ((required)), notificationchannel.title ((required))
- `GET /v1/notification-channels/all Get All` — Notification Channels

## Notification_Templates
- `POST /v1/notification-templates Create Notification` — Template
    - body: title ((required)), description ((required)), html ((required)), mjml ((required))
- `GET /v1/notification-templates/ Paginate Notification` — templates
- `DELETE /v1/notification-templates/:id Delete` — Notification Template
- `GET /v1/notification-templates/:id Get Notification` — Template
- `PATCH /v1/notification-templates/:id Update` — Notification Template
    - body: title ((required)), description ((required)), html ((required)), mjml ((required)), notificationtemplate.description ((required)), notificationtemplate.title ((required))
- `GET /v1/notification-templates/all Get All` — Notification Templates

## Notifications
- `GET /v1/notification-events` — Paginate Notifications
- `POST /v1/notification-events` — Create Notification
    - body: notification_template_id ((required)), model ((required)), action ((required)), subject ((required)), description ((required)), html ((optional)), markup ((optional)), text ((optional)), email ((optional)), notificationtemplate.description ((required)), notificationtemplate.title ((required))
- `POST /v1/notification-events` — Create Notification
    - body: notification_template_id ((required)), model ((required)), action ((required)), subject ((required)), description ((required)), html ((optional)), markup ((optional)), text ((optional)), email ((optional)), notificationtemplate.description ((required)), notificationtemplate.title ((required))
- `POST /v1/notification-events` — Create Notification
    - body: notification_template_id ((required)), model ((required)), action ((required)), subject ((required)), description ((required)), html ((optional)), markup ((optional)), text ((optional)), email ((optional)), notificationtemplate.description ((required)), notificationtemplate.title ((required))
- `GET /v1/notification-events/:id` — Get Notification
- `PATCH /v1/notification-events/:id` — Update Notification
    - body: notification_template_id ((required)), model ((required)), action ((required)), subject ((required)), description ((required)), html ((optional)), markup ((optional)), text ((optional)), email ((optional)), notificationtemplate.description ((required)), notificationtemplate.title ((required))
- `PATCH /v1/notification-events/:id` — Update Notification
    - body: notification_template_id ((required)), model ((required)), action ((required)), subject ((required)), description ((required)), html ((optional)), markup ((optional)), text ((optional)), email ((optional)), notificationtemplate.description ((required)), notificationtemplate.title ((required))
- `DELETE /v1/notification-events/:id Delete` — notification
- `GET /v1/notification-events/all` — Get All Notifications
- `POST /v1/notifications` — Create Notification
    - body: title ((required)), description ((required)), html ((required)), mjml ((required))
- `POST /v1/notifications` — Create Notification
    - body: title ((required)), description ((required)), html ((required)), mjml ((required))
- `GET /v1/notifications/ Paginate Notification` — s
- `GET /v1/notifications/:id` — Get Notification
- `DELETE /v1/notifications/:id Delete` — Notification
- `PATCH /v1/notifications/:id Update` — Notification
    - body: title ((required)), description ((required)), html ((required)), mjml ((required)), notification.description ((required)), notification.title ((required))
- `GET /v1/notifications/all Get All` — Notifications

## OAuth2
- `DELETE /v1/google-integration-authorize/{integration}` — Google_integration_auth
- `GET /v1/google-integration-consent-url` — Google_integration_consent_url
- `DELETE /v1/logout` — Logout
- `DELETE /v1/logout` — Logout
- `DELETE /v1/logout` — Logout
- `DELETE /v1/logout` — Logout
- `POST /v1/oauth/token` — Login (Client Credentials Grant)
    - body: client_id ((required)), client_secret ((required)), grant_type (must be `client_credentials` (required)), scope (you can leave it empty (optional))
- `POST /v1/oauth/token` — Login (Password Grant)
    - body: username (user email (required)), password (user password (required)), client_id ((required)), client_secret ((required)), grant_type (must be `password` (required)), scope (you can leave it empty (optional))
- `DELETE /v1/social-login` — Social_login
- `DELETE /v1/social-login-account` — Social_login_for_account_page
- `GET /v1/social-login-redirect` — Social_login_redirect
- `GET /v1/social-login-redirect-account` — Social_login_redirect_for_account_page
- `GET /v1/users/:id/mask` — MaskAsUser
- `GET /v1/users/remove-mask` — RemoveMaskAsUser

## Open_Invoice_Issued_for_Partner
- `GET /v1/open-invoices-issued-partner/:partner_id` — Get Invoices Issued

## Options
- `GET /v1/options` — Lists All Options
- `POST /v1/options` — Create Option
    - body: name ((required, max:255)), slug ((optional, max:255)), description ((optional)), value ((optional)), public ((optional)), data ((optional))
- `POST /v1/options` — Create Option
    - body: name ((required, max:255)), slug ((optional, max:255)), description ((optional)), value ((optional)), public ((optional)), data ((optional))
- `DELETE /v1/options/:id` — Delete Option
- `GET /v1/options/:id` — Get Option
- `PATCH /v1/options/:id` — Update Option
    - body: name ((required, max:255)), slug ((optional, max:255)), description ((optional)), value ((optional)), public ((optional)), data ((optional))
- `GET /v1/options/all` — Get all Options
- `GET /v1/options/all` — Get all Options

## Order
- `POST /v1/ordersaleshirt` — Endpoint title here..
    - body: parameters (here..)

## Order_Consumable_Items
- `GET /v1/order-consumable-items` — Paginate Order Consumable Items
- `POST /v1/order-consumable-items` — Create Order Consumable Item
    - body: order_consumable_id ((required, exists:orders_consumable.id)), product_id ((required, exists:products.id)), quantity ((required)), note ((optional))
- `DELETE /v1/order-consumable-items/:id` — Delete Order Consumable Items
- `PATCH /v1/order-consumable-items/:id` — Update Order Consumable Items
    - body: order_consumable_id ((required, exists:orders_consumable.id)), product_id ((required, exists:products.id)), quantity ((required)), note ((optional))
- `GET /v1/order-consumable-items/:id Get Order` — Consumable Items
- `GET /v1/order-consumable-items/all` — Get All Order Consumable Items

## Order_Consumables
- `GET /v1/orders-consumable` — Paginate Users
- `POST /v1/orders-consumable` — Create Order Consumable
    - body: user_id ((optional, exists:users.id)), document_type_id ((required, exists:document_types.id)), document_number ((required,.max:255)), reference_number ((optional, max:255)), internal_reference_number ((optional, max:255)), contact_name ((optional, max:255)), contact_email ((optional)), contact_phone ((optional, max:30)), contact_mobile ((optional, max:30)), contact_fax ((optional, max:30))
- `GET /v1/orders-consumable/:id` — Get Order Consumables
- `PATCH /v1/orders-consumable/:id` — Update consumable order
    - body: user_id ((optional, exists:users.id)), document_type_id ((required, exists:document_types.id)), document_number ((required,.max:255)), reference_number ((optional, max:255)), internal_reference_number ((optional, max:255)), contact_name ((optional, max:255)), contact_email ((optional)), contact_phone ((optional, max:30)), contact_mobile ((optional, max:30)), contact_fax ((optional, max:30))
- `DELETE /v1/orders-consumable/:id Delete` — OrderConsumables
- `GET /v1/orders-consumable/all` — Get All Order Consumables

## Order_Purchase_Items
- `GET /v1/order-purchase-items` — Paginate Order Purchase Items
- `POST /v1/order-purchase-items` — Create Order Purchase
    - body: order_purchase_id ((required, exists:orders_purchase.id)), product_id ((required, exists:products.id)), reference_number ((optional, max:255)), description (String), quantity (Numeric), quantity_undelivered (Numeric), amount (Numeric), discount_rate (Numeric), amount_discount (Numeric), tax_rate (Numeric), amount_vat (Numeric), weight (Numeric), stock_at_partner (Numeric), date_delivery_expected ((optional)), date_delivery_wanted ((optional)), date_delivery_confirmed (Date), date_partner_last (Date), date_delivery_confirmed_final (Date), note ((optional)), date_delivery_actual ((optional))
- `DELETE /v1/order-purchase-items/:id` — Delete order purchase item
- `GET /v1/order-purchase-items/:id` — Get Order Purchase Item
- `PATCH /v1/order-purchase-items/:id` — Update Order Purchase Item
    - body: order_purchase_id ((required, exists:orders_purchase.id)), product_id ((required, exists:products.id)), reference_number ((optional, max:255)), description (String), quantity (Numeric), quantity_undelivered (Numeric), amount (Numeric), discount_rate (Numeric), amount_discount (Numeric), tax_rate (Numeric), amount_vat (Numeric), weight (Numeric), stock_at_partner (Numeric), date_delivery_expected ((optional)), date_delivery_wanted ((optional)), date_delivery_confirmed (Date), date_partner_last (Date), date_delivery_confirmed_final (Date), note ((optional)), date_delivery_actual ((optional))
- `GET /v1/order-purchase-items/all` — Get All Order Purchase Items

## Order_Purchases
- `GET /v1/orders-purchase` — Paginate Order Purchases
- `GET /v1/orders-purchase` — Paginate Order Purchases
- `GET /v1/orders-purchase` — Paginate Order Purchases
- `GET /v1/orders-purchase` — Paginate Order Purchases
- `POST /v1/orders-purchase` — Create Order Purchase
    - body: partner_id ((optiona, exists:partners.id)), user_id ((optional, exists:users.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional, max:255)), internal_reference_number ((optional, max:255)), transit_information ((optional)), contact_name ((optional, max:255)), contact_email ((optional)), contact_phone ((optional, max:30)), contact_mobile ((optional, max:30)), contact_fax ((optional, max:30)), currency_code_id ((optional, alpha, exists:currency_codes.id)), currency_rate ((optional)), amount_total_currency ((optional)), amount_total ((optional)), print_footer ((optional)), email_purchase_sent ((optional)), email_inquiry_sent ((optional)), email_confirmation_reminder_sent ((optional))
- `POST /v1/orders-purchase` — Create Order Purchase
    - body: partner_id ((optiona, exists:partners.id)), user_id ((optional, exists:users.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional, max:255)), internal_reference_number ((optional, max:255)), transit_information ((optional)), contact_name ((optional, max:255)), contact_email ((optional)), contact_phone ((optional, max:30)), contact_mobile ((optional, max:30)), contact_fax ((optional, max:30)), currency_code_id ((optional, alpha, exists:currency_codes.id)), currency_rate ((optional)), amount_total_currency ((optional)), amount_total ((optional)), print_footer ((optional)), email_purchase_sent ((optional)), email_inquiry_sent ((optional)), email_confirmation_reminder_sent ((optional))
- `DELETE /v1/orders-purchase/:id` — Delete Order Purchase
- `GET /v1/orders-purchase/:id` — Get Order Purchase
- `PATCH /v1/orders-purchase/:id` — Update Order Purchase
    - body: partner_id ((optiona, exists:partners.id)), user_id ((optional, exists:users.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional, max:255)), internal_reference_number ((optional, max:255)), transit_information ((optional)), contact_name ((optional, max:255)), contact_email ((optional)), contact_phone ((optional, max:30)), contact_mobile ((optional, max:30)), contact_fax ((optional, max:30)), currency_code_id ((optional, alpha, exists:currency_codes.id)), currency_rate ((optional)), amount_total_currency ((optional)), amount_total ((optional)), print_footer ((optional)), email_purchase_sent ((optional)), email_inquiry_sent ((optional)), email_confirmation_reminder_sent ((optional))
- `PATCH /v1/orders-purchase/:id` — Update Order Purchase
    - body: partner_id ((optiona, exists:partners.id)), user_id ((optional, exists:users.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional, max:255)), internal_reference_number ((optional, max:255)), transit_information ((optional)), contact_name ((optional, max:255)), contact_email ((optional)), contact_phone ((optional, max:30)), contact_mobile ((optional, max:30)), contact_fax ((optional, max:30)), currency_code_id ((optional, alpha, exists:currency_codes.id)), currency_rate ((optional)), amount_total_currency ((optional)), amount_total ((optional)), print_footer ((optional)), email_purchase_sent ((optional)), email_inquiry_sent ((optional)), email_confirmation_reminder_sent ((optional))
- `GET /v1/orders-purchase/all` — Get All Order Purchases
- `GET /v1/purchase-requirement-for-sales-orders-by-fifo Paginate Purchase Requirement For Sales` — Orders By Fifo
- `GET /v1/purchase-requirement-for-sales-orders-by-fifo/all Get All Purchase Requirement For` — Sales Orders By Fifo

## Order_Quote_Items
- `GET /v1/order-quote-items` — Paginate Order Quote Items
- `POST /v1/order-quote-items` — Create Order Quote Items
    - body: parent_id ((optional, exists:order_quote_items.id)), order_quote_id ((required, exists:orders_quote.id)), sales_forecast_item_id ((optional, exists:sales_forecast_items.id)), product_id ((required, exists:products.id)), reference_number ((optional, max:255)), quantity ((required)), amount ((required)), discount_rate ((required)), amount_discount ((required)), tax_rate ((required)), amount_vat ((required)), amount_total ((required)), weight ((required)), bundled ((optional)), note ((optional))
- `GET /v1/order-quote-items/:id` — Get Order Quote Items
- `PATCH /v1/order-quote-items/:id` — Update Order Quote Items
    - body: partner_id ((optional, exists:partners.id)), user_id ((optional, exists:users.id)), shipping_method_id ((optional, exists:shipping_methods.id)), payment_method_id ((optional, exists:payment_methods.id)), payment_term_id ((optional, exists:payment_terms.id)), rental_warehouse_location_id ((optional, exists:warehouse_locations.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional, max:255)), internal_reference_number ((optional, max:255)), contact_name ((optional, max:255)), contact_email ((optional)), contact_phone ((optional, max:30)), contact_mobile ((optional, max:30)), contact_fax ((optional, max:30)), billing_company ((optional, max:255)), billing_address1 ((optional, max:255)), billing_address2 ((optional, max:255)), billing_post ((optional, max:255)), billing_city ((optional, max:255)), billing_state_id ((optional,alpha, exists:states.id)), billing_country_id ((optional, alpha, exists:countries.id)), vatid ((optional, max:25)), shipping_company ((optional, max:255)), shipping_address1 ((optional, max:255)), shipping_address2 ((optional, max:255)), shipping_post ((optional, max:255)), shipping_city ((optional, max:255)), shipping_state_id ((optional, max:25)), shipping_country_id ((optional)), shipping_account ((optional)), shipping_vatid ((optional, max:25)), end_customer_industry ((optional)), end_customer_solution_area ((optional)), end_customer_solution ((optional)), end_customer_application_description ((optional)), end_customer_company ((optional)), end_customer_city ((optional)), end_customer_country_id ((optional, alpha, exists:countries.id)), currency_code_id ((optional, alpha, exists:currency_codes.id)), currency_rate ((optional)), amount_total_currency ((optional)), amount_total ((optional)), weight ((optional)), financing_rate ((optional)), amount_financing ((optional)), amount_shipping ((optional)), amount_packaging ((optional)), quote_probability ((optional)), quote_closing_date ((optional, format:Y-m-d H:i:s')), print_footer ((optional)), quote_common_list ((optional)), crm_offer_number ((optional, max:50)), crm_number ((optional, max:50)), configurator_data ((optional)), price_list_id ((optional, exists:price_lists.id)), price_list_version_id ((optional, exists:price_list_versions.id)), end_customer_id ((optional, exists:partners.id))
- `DELETE /v1/order-quote-items/:id Delete Order Quote` — Items
- `GET /v1/order-quote-items/all` — Get All Order Quote Items

## Order_Quotes
- `GET /v1/orders-quote` — Paginate Order Quotes
- `POST /v1/orders-quote` — Create Order Quotes
    - body: partner_id ((optional, exists:partners.id)), user_id ((optional, exists:users.id)), shipping_method_id ((optional, exists:shipping_methods.id)), payment_method_id ((optional, exists:payment_methods.id)), payment_term_id ((optional, exists:payment_terms.id)), rental_warehouse_location_id ((optional, exists:warehouse_locations.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional, max:255)), internal_reference_number ((optional, max:255)), contact_name ((optional, max:255)), contact_email ((optional)), contact_phone ((optional, max:30)), contact_mobile ((optional, max:30)), contact_fax ((optional, max:30)), billing_company ((optional, max:255)), billing_address1 ((optional, max:255)), billing_address2 ((optional, max:255)), billing_post ((optional, max:255)), billing_city ((optional, max:255)), billing_state_id ((optional,alpha, exists:states.id)), billing_country_id ((optional, alpha, exists:countries.id)), vatid ((optional, max:25)), shipping_company ((optional, max:255)), shipping_address1 ((optional, max:255)), shipping_address2 ((optional, max:255)), shipping_post ((optional, max:255)), shipping_city ((optional, max:255)), shipping_state_id ((optional, max:25)), shipping_country_id ((optional)), shipping_account ((optional)), shipping_vatid ((optional, max:25)), end_customer_industry ((optional)), end_customer_solution_area ((optional)), end_customer_solution ((optional)), end_customer_application_description ((optional)), end_customer_company ((optional)), end_customer_city ((optional)), end_customer_country_id ((optional, alpha, exists:countries.id)), currency_code_id ((optional, alpha, exists:currency_codes.id)), currency_rate ((optional)), amount_total_currency ((optional)), amount_total ((optional)), weight ((optional)), financing_rate ((optional)), amount_financing ((optional)), amount_shipping ((optional)), amount_packaging ((optional)), quote_probability ((optional)), quote_closing_date ((optional, format:Y-m-d H:i:s')), print_footer ((optional)), quote_common_list ((optional)), crm_offer_number ((optional, max:50)), crm_number ((optional, max:50)), configurator_data ((optional)), price_list_id ((optional, exists:price_lists.id)), price_list_version_id ((optional, exists:price_list_versions.id)), end_customer_id ((optional, exists:partners.id))
- `DELETE /v1/orders-quote/:id` — Delete Order Quotes
- `GET /v1/orders-quote/:id` — Get Order Quotes
- `PATCH /v1/orders-quote/:id` — Update Order Quotes
    - body: partner_id ((optional, exists:partners.id)), user_id ((optional, exists:users.id)), shipping_method_id ((optional, exists:shipping_methods.id)), payment_method_id ((optional, exists:payment_methods.id)), payment_term_id ((optional, exists:payment_terms.id)), rental_warehouse_location_id ((optional, exists:warehouse_locations.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional, max:255)), internal_reference_number ((optional, max:255)), contact_name ((optional, max:255)), contact_email ((optional)), contact_phone ((optional, max:30)), contact_mobile ((optional, max:30)), contact_fax ((optional, max:30)), billing_company ((optional, max:255)), billing_address1 ((optional, max:255)), billing_address2 ((optional, max:255)), billing_post ((optional, max:255)), billing_city ((optional, max:255)), billing_state_id ((optional,alpha, exists:states.id)), billing_country_id ((optional, alpha, exists:countries.id)), vatid ((optional, max:25)), shipping_company ((optional, max:255)), shipping_address1 ((optional, max:255)), shipping_address2 ((optional, max:255)), shipping_post ((optional, max:255)), shipping_city ((optional, max:255)), shipping_state_id ((optional, max:25)), shipping_country_id ((optional)), shipping_account ((optional)), shipping_vatid ((optional, max:25)), end_customer_industry ((optional)), end_customer_solution_area ((optional)), end_customer_solution ((optional)), end_customer_application_description ((optional)), end_customer_company ((optional)), end_customer_city ((optional)), end_customer_country_id ((optional, alpha, exists:countries.id)), currency_code_id ((optional, alpha, exists:currency_codes.id)), currency_rate ((optional)), amount_total_currency ((optional)), amount_total ((optional)), weight ((optional)), financing_rate ((optional)), amount_financing ((optional)), amount_shipping ((optional)), amount_packaging ((optional)), quote_probability ((optional)), quote_closing_date ((optional, format:Y-m-d H:i:s')), print_footer ((optional)), quote_common_list ((optional)), crm_offer_number ((optional, max:50)), crm_number ((optional, max:50)), configurator_data ((optional)), price_list_id ((optional, exists:price_lists.id)), price_list_version_id ((optional, exists:price_list_versions.id)), end_customer_id ((optional, exists:partners.id))
- `GET /v1/orders-quote/all` — Get All Order Quotes

## Order_Sale_Items
- `GET /v1/order-sale-items` — Paginate Order Sale Items
- `POST /v1/order-sale-items` — Create Order Sale Items
    - body: parent_id ((optional, exists:order_sale_items.id)), order_sale_id ((required, exists:orders_sale.id)), product_id ((required, exists:products.id)), packing_product_id ((optional, exists:products.id)), origin_county_id ((optional, sometimes, alpha, max:2, exists:countries.id)), tariff_code_id ((optional, exists:tariff_codes.id)), saop_tax_rate_id ((optional, exists:tax_rates.id)), reference_number ((optional, max:255)), quantity ((required)), amount ((required)), discount_rate ((required)), amount_discount ((required)), tax_rate ((required)), amount_vat ((required)), amount_total ((required)), amount_discount_rep ((optional)), amount_rep ((optional)), weight ((optional)), date_delivery_wanted ((optional, format:Y-m-d H:i:s)), date_delivery_expected ((optional, format:Y-m-d H:i:s)), date_delivery_confirmed ((optional, format:Y-m-d H:i:s)), date_delivery_actual ((optional, format:Y-m-d H:i:s)), bundled ((optional)), note ((optional))
- `POST /v1/order-sale-items` — Create Order Sale Items
    - body: parent_id ((optional, exists:order_sale_items.id)), order_sale_id ((required, exists:orders_sale.id)), product_id ((required, exists:products.id)), packing_product_id ((optional, exists:products.id)), origin_county_id ((optional, sometimes, alpha, max:2, exists:countries.id)), tariff_code_id ((optional, exists:tariff_codes.id)), saop_tax_rate_id ((optional, exists:tax_rates.id)), reference_number ((optional, max:255)), quantity ((required)), amount ((required)), discount_rate ((required)), amount_discount ((required)), tax_rate ((required)), amount_vat ((required)), amount_total ((required)), amount_discount_rep ((optional)), amount_rep ((optional)), weight ((optional)), date_delivery_wanted ((optional, format:Y-m-d H:i:s)), date_delivery_expected ((optional, format:Y-m-d H:i:s)), date_delivery_confirmed ((optional, format:Y-m-d H:i:s)), date_delivery_actual ((optional, format:Y-m-d H:i:s)), bundled ((optional)), note ((optional))
- `DELETE /v1/order-sale-items/:id` — Delete Order Sale Items
- `GET /v1/order-sale-items/:id` — Get Order Sale Items
- `PATCH /v1/order-sale-items/:id` — Update Order Sale Items
    - body: parent_id ((optional, exists:order_sale_items.id)), order_sale_id ((required, exists:orders_sale.id)), product_id ((required, exists:products.id)), packing_product_id ((optional, exists:products.id)), origin_county_id ((optional, sometimes, alpha, max:2, exists:countries.id)), tariff_code_id ((optional, exists:tariff_codes.id)), saop_tax_rate_id ((optional, exists:tax_rates.id)), reference_number ((optional, max:255)), quantity ((required)), amount ((required)), discount_rate ((required)), amount_discount ((required)), tax_rate ((required)), amount_vat ((required)), amount_total ((required)), amount_discount_rep ((optional)), amount_rep ((optional)), weight ((optional)), date_delivery_wanted ((optional, format:Y-m-d H:i:s)), date_delivery_expected ((optional, format:Y-m-d H:i:s)), date_delivery_confirmed ((optional, format:Y-m-d H:i:s)), date_delivery_actual ((optional, format:Y-m-d H:i:s)), bundled ((optional)), note ((optional))
- `POST /v1/order-sale-items/:id/link-serials` — Link order serials
    - body: parent_id ((optional, exists:order_sale_items.id)), order_sale_id ((required, exists:orders_sale.id)), product_id ((required, exists:products.id)), packing_product_id ((optional, exists:products.id)), origin_county_id ((optional, sometimes, alpha, max:2, exists:countries.id)), tariff_code_id ((optional, exists:tariff_codes.id)), saop_tax_rate_id ((optional, exists:tax_rates.id)), reference_number ((optional, max:255)), quantity ((required)), amount ((required)), discount_rate ((required)), amount_discount ((required)), tax_rate ((required)), amount_vat ((required)), amount_total ((required)), amount_discount_rep ((optional)), amount_rep ((optional)), weight ((optional)), date_delivery_wanted ((optional, format:Y-m-d H:i:s)), date_delivery_expected ((optional, format:Y-m-d H:i:s)), date_delivery_confirmed ((optional, format:Y-m-d H:i:s)), date_delivery_actual ((optional, format:Y-m-d H:i:s)), bundled ((optional)), note ((optional))
- `GET /v1/order-sale-items/:id/work-order-items` — Get work orders
- `GET /v1/order-sale-items/all` — Get All Order Sale Items

## Order_Sales
- `GET /v1/orders-sale` — Paginate Order Sales
- `POST /v1/orders-sale` — Create Order Sales
    - body: order_quote_id ((optional, exists:orders_quote.id)), partner_id ((optional, exists:partners.id)), user_id ((optional, exists:users.id)), shipping_method_id ((optional, exists:shipping_methods.id)), payment_method_id ((optional, exists:payment_methods.id)), payment_term_id ((optional, exists:payment_terms.id)), rental_warehouse_location_id ((optional, exists:warehouse_locations.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional, max:255)), internal_reference_number ((optional, max:255)), contact_name ((optional, max:255)), contact_email ((optional)), contact_phone ((optional, max:255)), contact_mobile ((optional, max:255)), contact_fax ((optional, max:255)), billing_company ((optional, max:255)), billing_address1 ((optional, max:255)), billing_address2 ((optional, max:255)), billing_post ((optional, max:255)), billing_city ((optional, max:255)), billing_state_id ((optional, alpha, exists:states.id)), billing_country_id ((optional, alpha, exists:countries.id)), vatid ((optional, max:25)), shipping_company ((optional,max:255)), shipping_address1 ((optional, max:255)), shipping_address2 ((optional, max:255)), shipping_post ((optional, max:255)), shipping_city ((optional, max:255)), shipping_state_id ((optional, alpha, exists:states.id)), shipping_country_id ((optional, alpha, exists:countries.id)), shipping_account ((optional, max:255)), shipping_vatid ((optional, max:25)), end_customer_industry ((optional)), end_customer_solution ((optional)), end_customer_solution_area ((optional)), end_customer_application_description ((optional)), end_customer_company ((optional)), end_customer_city ((optional)), end_customer_country_id ((optional, alpha, exists:countries.id)), currency_code_id ((optional, alpha, exists:currency_codes.id)), currency_rate ((required)), amount_total_currency ((required)), amount_total ((required)), amount_rep ((optional)), amount_vat ((optional)), amount_base_vat ((optional)), weight ((required)), financing_rate ((required)), amount_financing ((required)), amount_shipping ((required)), amount_packaging ((optional)), amount_production ((optional)), production_rate ((optional)), rented_from ((required, format:Y-m-d H:i:s)), rented_to ((required, format:Y-m-d H:i:s)), date_delivery_wanted ((required, format:Y-m-d H:i:s)), date_delivery_expected ((required, format:Y-m-d H:i:s)), date_delivery_actual ((required, format:Y-m-d H:i:s)), date_internal ((optional, format:Y-m-d H:i:s)), date_expected_plan ((optional, format:Y-m-d H:i:s)), demo ((optional, format:Y-m-d H:i:s)), print_footer ((optional)), quote_common_list ((optional)), crm_offer_number ((optional, max:50)), crm_number ((optional, max:50)), configurator_data ((optional)), price_list_id ((optional, exists:price_lists.id)), price_list_version_id ((optional, exists:price_list_versions.id)), is_eu ((optional)), calculate_vat ((optional)), selected_partner_billing_address_id ((optional, exists:addresses.id)), selected_partner_shipping_address_id ((optional, exists:addresses.id)), service_import_mrn ((optional, max:255)), date_service_import ((optional, format:Y-m-d H:i:s)), amount_service_import ((optional)), weight_neto ((optional)), weight_gross ((optional)), ceo_full_name ((optional, max:255)), consignee_id ((optional, exists:partners.id)), end_customer_id ((optional, exists:partners.id)), euc_checked ((optional))
- `DELETE /v1/orders-sale/:id` — Delete Order Sales
- `GET /v1/orders-sale/:id` — Get Order Sales
- `GET /v1/orders-sale/:id` — Get Order Sales
- `PATCH /v1/orders-sale/:id` — Update Order Sales
    - body: order_quote_id ((optional, exists:orders_quote.id)), partner_id ((optional, exists:partners.id)), user_id ((optional, exists:users.id)), shipping_method_id ((optional, exists:shipping_methods.id)), payment_method_id ((optional, exists:payment_methods.id)), payment_term_id ((optional, exists:payment_terms.id)), rental_warehouse_location_id ((optional, exists:warehouse_locations.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional, max:255)), internal_reference_number ((optional, max:255)), contact_name ((optional, max:255)), contact_email ((optional)), contact_phone ((optional, max:255)), contact_mobile ((optional, max:255)), contact_fax ((optional, max:255)), billing_company ((optional, max:255)), billing_address1 ((optional, max:255)), billing_address2 ((optional, max:255)), billing_post ((optional, max:255)), billing_city ((optional, max:255)), billing_state_id ((optional, alpha, exists:states.id)), billing_country_id ((optional, alpha, exists:countries.id)), vatid ((optional, max:25)), shipping_company ((optional,max:255)), shipping_address1 ((optional, max:255)), shipping_address2 ((optional, max:255)), shipping_post ((optional, max:255)), shipping_city ((optional, max:255)), shipping_state_id ((optional, alpha, exists:states.id)), shipping_country_id ((optional, alpha, exists:countries.id)), shipping_account ((optional, max:255)), shipping_vatid ((optional, max:25)), end_customer_industry ((optional)), end_customer_solution ((optional)), end_customer_solution_area ((optional)), end_customer_application_description ((optional)), end_customer_company ((optional)), end_customer_city ((optional)), end_customer_country_id ((optional, alpha, exists:countries.id)), currency_code_id ((optional, alpha, exists:currency_codes.id)), currency_rate ((required)), amount_total_currency ((required)), amount_total ((required)), amount_rep ((optional)), amount_vat ((optional)), amount_base_vat ((optional)), weight ((required)), financing_rate ((required)), amount_financing ((required)), amount_shipping ((required)), amount_packaging ((optional)), amount_production ((optional)), production_rate ((optional)), rented_from ((required, format:Y-m-d H:i:s)), rented_to ((required, format:Y-m-d H:i:s)), date_delivery_wanted ((required, format:Y-m-d H:i:s)), date_delivery_expected ((required, format:Y-m-d H:i:s)), date_delivery_actual ((required, format:Y-m-d H:i:s)), date_internal ((optional, format:Y-m-d H:i:s)), date_expected_plan ((optional, format:Y-m-d H:i:s)), demo ((optional, format:Y-m-d H:i:s)), print_footer ((optional)), quote_common_list ((optional)), crm_offer_number ((optional, max:50)), crm_number ((optional, max:50)), configurator_data ((optional)), price_list_id ((optional, exists:price_lists.id)), price_list_version_id ((optional, exists:price_list_versions.id)), is_eu ((optional)), calculate_vat ((optional)), selected_partner_billing_address_id ((optional, exists:addresses.id)), selected_partner_shipping_address_id ((optional, exists:addresses.id)), service_import_mrn ((optional, max:255)), date_service_import ((optional, format:Y-m-d H:i:s)), amount_service_import ((optional)), weight_neto ((optional)), weight_gross ((optional)), ceo_full_name ((optional, max:255)), consignee_id ((optional, exists:partners.id)), end_customer_id ((optional, exists:partners.id)), euc_checked ((optional))
- `GET /v1/orders-sale/:id/calibration-report-recursive-xml` — Get Serials calibration recursive xml
- `POST /v1/orders-sale/:id/documents` — Create Documents for Sale Order
    - body: partner_id ((optional))
- `DELETE /v1/orders-sale/:id/force` — Force Delete Order Sales
- `POST /v1/orders-sale/:id/invoice` — Create Invoice for Sale Order
    - body: items ((required)), partner_id ((required)), sale_type_id ((required)), date_payment ((required)), date_invoice ((required))
- `GET /v1/orders-sale/:id/recalculate-amount` — Recalculate amount
- `GET /v1/orders-sale/:id/recalculate-amount-rep` — Recalculate amount rep
- `GET /v1/orders-sale/:id/recalculate-amount-rep-m2m` — Recalculate amount rep M2M
- `POST /v1/orders-sale/:id/send-expected-delivery-date-notification Send expected` — delivery date notification
    - body: to ((required)), subject ((required)), content ((required)), cc ((optional)), bcc ((optional))
- `GET /v1/orders-sale/all` — Get All Order Sales
- `PATCH /v1/orders-sale/split` — Split Order Sale
- `GET /v1/orders-sale/{id}/iso-calibration-report-recursive` — Get Serials Iso calibration

## Packing_Boxes
- `GET /v1/packing-boxes` — Paginate Packing Boxes
- `POST /v1/packing-boxes` — Create Packing Box
    - body: packing_list_id ((required, exists:packing_lists.id)), name ((required, max:255)), width ((optional)), height ((optional)), depth ((optional)), net_weight ((required)), gross_weight ((required))
- `DELETE /v1/packing-boxes/:id` — Delete Packing Box
- `GET /v1/packing-boxes/:id` — Get Packing Box
- `PATCH /v1/packing-boxes/:id` — Update Packing Box
    - body: packing_list_id ((required, exists:packing_lists.id)), name ((required, max:255)), width ((optional)), height ((optional)), depth ((optional)), net_weight ((required)), gross_weight ((required))
- `GET /v1/packing-boxes/all` — Get All Packing Boxes

## Packing_List_Items
- `GET /v1/packing-list-items` — Paginate Packing List Items
- `POST /v1/packing-list-items` — Create Packing List Item
    - body: packing_list_id ((required, exists:packing_lists.id)), order_sale_item_id ((optional, exists:order_sale_items.id)), packing_box_id ((optional, exists:packing_boxes.id)), product_id ((required, exists:products.id)), origin_country_id ((optional, sometimes, alpha, max:2, exists:countries.id)), tariff_code_id ((optional, exists:tariff_codes.id)), saop_tax_rate_id ((optional, exists:tax_rates.id)), name ((required, max:255)), description ((optional)), reference_number ((optional)), weight ((required)), quantity ((required))
- `DELETE /v1/packing-list-items/:id` — Delete Packing List Item
- `GET /v1/packing-list-items/:id` — Get Packing List Item
- `PATCH /v1/packing-list-items/:id` — Update Packing List Item
    - body: packing_list_id ((required, exists:packing_lists.id)), order_sale_item_id ((optional, exists:order_sale_items.id)), packing_box_id ((optional, exists:packing_boxes.id)), product_id ((required, exists:products.id)), origin_country_id ((optional, sometimes, alpha, max:2, exists:countries.id)), tariff_code_id ((optional, exists:tariff_codes.id)), saop_tax_rate_id ((optional, exists:tax_rates.id)), name ((required, max:255)), description ((optional)), reference_number ((optional)), weight ((required)), quantity ((required))
- `GET /v1/packing-list-items/all` — Get All Packing List Items

## Packing_Lists
- `GET /v1/packing-lists` — Paginate Packing Lists
- `POST /v1/packing-lists` — Create Packing List
    - body: document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), billing_company ((optional,max:255)), billing_address1 ((optional, max:255)), billing_address2 ((optional, max:255)), billing_post ((optional, max:255)), billing_city ((optional, max:255)), billing_state_id ((optional, alpha, exists:states.id)), billing_country_id ((optional, alpha, exists:countries.id)), vatid ((optional, max:25)), shipping_company ((optional, max:255)), shipping_address1 ((optional, max:255)), shipping_address2 ((optional, max:255)), shipping_post ((optional, max:255)), shipping_city ((optional, max:255)), shipping_state_id ((optional, alpha, exists:states.id)), shipping_country_id ((optional, alpha, exists:countries.id)), print_footer ((optional))
- `DELETE /v1/packing-lists/:id` — Delete Packing List
- `GET /v1/packing-lists/:id` — Get Packing List
- `PATCH /v1/packing-lists/:id` — Update Packing List
    - body: document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), billing_company ((optional,max:255)), billing_address1 ((optional, max:255)), billing_address2 ((optional, max:255)), billing_post ((optional, max:255)), billing_city ((optional, max:255)), billing_state_id ((optional, alpha, exists:states.id)), billing_country_id ((optional, alpha, exists:countries.id)), vatid ((optional, max:25)), shipping_company ((optional, max:255)), shipping_address1 ((optional, max:255)), shipping_address2 ((optional, max:255)), shipping_post ((optional, max:255)), shipping_city ((optional, max:255)), shipping_state_id ((optional, alpha, exists:states.id)), shipping_country_id ((optional, alpha, exists:countries.id)), print_footer ((optional))
- `GET /v1/packing-lists/all` — Get All Packing Lists

## Partner_Applications
- `GET /v1/partner-applications` — Paginate partner applications

## Partner_types
- `GET /v1/partner-types` — Paginate Partners
- `GET /v1/partner-types/all` — Get All Partner types

## Partners
- `GET /v1/partners` — Paginate Partners
- `POST /v1/partners` — Create Partner
    - body: parent_id ((optional)), partner_type_id ((optional, exists:partner_types.id, nullable)), short_name ((optional, max:255)), long_name ((optional, max:255)), contact_phone ((optional, max:20)), contact_mobile ((optional, max:20)), contact_fax ((optional, max:20)), contact_email ((optional)), ordering_email ((optional)), web ((optional)), vat_number ((optional, max:255)), vatid ((optional, max:20)), bank_swift_code ((optional, max:11, unique:partners, bank_swift_code)), tracking_url ((optional)), code ((optional)), payment_term_id ((optional, exists:payment_terms.id)), default_expense_event_id ((optional, exists:expense_events.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), delivery_time ((optional)), transit_time ((optional)), external_documents_url ((optional)), accounting_email ((optional)), registration_number ((optional))
- `DELETE /v1/partners/:id` — Delete Partner
- `GET /v1/partners/:id` — Get Partner
- `PATCH /v1/partners/:id` — Update Partner
    - body: parent_id ((optional)), partner_type_id ((optional, exists:partner_types.id, nullable)), short_name ((optional, max:255)), long_name ((optional, max:255)), contact_phone ((optional, max:20)), contact_mobile ((optional, max:20)), contact_fax ((optional, max:20)), contact_email ((optional)), ordering_email ((optional)), web ((optional)), vat_number ((optional, max:255)), vatid ((optional, max:20)), bank_swift_code ((optional, max:11, unique:partners, bank_swift_code)), tracking_url ((optional)), code ((optional)), payment_term_id ((optional, exists:payment_terms.id)), default_expense_event_id ((optional, exists:expense_events.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), delivery_time ((optional)), transit_time ((optional)), external_documents_url ((optional)), accounting_email ((optional)), registration_number ((optional))
- `GET /v1/partners/all` — Get All Partners
- `POST /v1/partners/m2m` — Create Partner M2M
    - body: parent_id ((optional)), partner_type_id ((optional, exists:partner_types.id, nullable)), short_name ((optional, max:255)), long_name ((optional, max:255)), contact_phone ((optional, max:20)), contact_mobile ((optional, max:20)), contact_fax ((optional, max:20)), contact_email ((optional)), ordering_email ((optional)), web ((optional)), vat_number ((optional, max:255)), vatid ((optional, max:20)), bank_swift_code ((optional, max:11, unique:partners, bank_swift_code)), tracking_url ((optional)), code ((optional)), payment_term_id ((optional, exists:payment_terms.id)), default_expense_event_id ((optional, exists:expense_events.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), delivery_time ((optional)), transit_time ((optional)), external_documents_url ((optional)), accounting_email ((optional)), registration_number ((optional))
- `GET /v1/partners/root-partner` — Get Root Partner

## Payment_Methods
- `GET /v1/payment-methods` — Paginate Payment Methods
- `POST /v1/payment-methods` — Create Payment Method
    - body: name ((required, max:255))
- `DELETE /v1/payment-methods/:id` — Delete Payment Method
- `GET /v1/payment-methods/:id` — Get Payment Method
- `PATCH /v1/payment-methods/:id` — Update Payment Method
    - body: name ((required, max:255))
- `GET /v1/payment-methods/all` — Get All Payment Methods

## Payment_Terms
- `GET /v1/payment-terms` — Paginate Payment Terms
- `POST /v1/payment-terms` — Create Payment Term
- `DELETE /v1/payment-terms/:id` — Delete Payment Term
- `GET /v1/payment-terms/:id` — Get Payment Term
- `PATCH /v1/payment-terms/:id` — Update Payment Term
    - body: name ((required, max:255)), days ((required)), financing_rate ((required)), description ((optional))
- `GET /v1/payment-terms/all` — Get All Payment Terms

## PerformanceReviews
- `GET /v1/performance-reviews/:company_strategy_id/export` — Get PerformanceReviews

## Permissions
- `GET /v1/permissions` — Paginate Permission
- `POST /v1/permissions` — Create a Permission
    - body: name ((required, unique:permissions, name)), guard_name ((required, in:api, web)), description ((optional)), display_name ((required)), group ((optional))
- `DELETE /v1/permissions/:id` — Delete a Permission
- `GET /v1/permissions/:id` — Find a Permission by ID
- `PATCH /v1/permissions/:id` — Update Permission
    - body: name ((required, unique:permissions, name)), guard_name ((required, in:api, web)), description ((optional)), display_name ((required)), group ((optional))
- `GET /v1/permissions/all` — Paginate Permissions

## Price_Lists
- `GET /v1/price-list-versions` — Paginate Price Lists
- `POST /v1/price-list-versions` — Create Price Category List
    - body: price_list_id ((required, exists:price_lists.id)), parent_id ((optional, exists:price_list_versions.id)), name ((required, max:255)), description ((optional)), valid_from ((optional, format:Y-m-d H:i:s)), valid_to ((optional, format:Y-m-d H:i:s))
- `POST /v1/price-list-versions` — Create Price Category List
    - body: price_list_id ((required, exists:price_lists.id)), parent_id ((optional, exists:price_list_versions.id)), name ((required, max:255)), description ((optional)), valid_from ((optional, format:Y-m-d H:i:s)), valid_to ((optional, format:Y-m-d H:i:s))
- `DELETE /v1/price-list-versions/:id` — Delete Price Lists
- `GET /v1/price-list-versions/:id` — Get Price Lists
- `PATCH /v1/price-list-versions/:id` — Update Price Lists
    - body: price_list_id ((required, exists:price_lists.id)), parent_id ((optional, exists:price_list_versions.id)), name ((required, max:255)), description ((optional)), valid_from ((optional, format:Y-m-d H:i:s)), valid_to ((optional, format:Y-m-d H:i:s))
- `GET /v1/price-list-versions/all` — Get All Price Lists
- `GET /v1/price-list-versions/all` — Get All Price Lists
- `GET /v1/price-lists` — Paginate Price Lists
- `POST /v1/price-lists` — Create Price Category List
    - body: parent_id ((exists:price_lists.id)), currency_code_id ((alpha, exists:currency_codes.id)), name ((required, max:255)), description ((optional)), price_list_source_id ((required, max:255)), price_round_precision ((required, max:255)), is_end_user ((optional)), is_master ((optinal))
- `DELETE /v1/price-lists/:id` — Delete Price Lists
- `GET /v1/price-lists/:id` — Get Price Lists
- `GET /v1/price-lists/:id` — Get Price Lists
- `PATCH /v1/price-lists/:id` — Update Price Lists
    - body: parent_id ((exists:price_lists.id)), currency_code_id ((alpha, exists:currency_codes.id)), name ((required, max:255)), description ((optional)), price_list_source_id ((required, max:255)), price_round_precision ((required, max:255)), is_end_user ((optional)), is_master ((optinal))
- `GET /v1/price-lists/all` — Get All Price Lists

## Price_Templates
- `GET /v1/price-templates` — Paginate Price Templates
- `POST /v1/price-templates` — Create Price Templates
    - body: name ((required, max:255)), description ((optional))
- `DELETE /v1/price-templates/:id` — Delete Price Templates
- `GET /v1/price-templates/:id` — Get Price Templates
- `PATCH /v1/price-templates/:id` — Update Price Templates
    - body: name ((required, max:255)), description ((optional))
- `GET /v1/price-templates/all` — Get All Price Templates

## PrintSigners
- `GET /v1/print-signers` — Lists All Print Signers
- `POST /v1/print-signers` — Create New Print Signers
- `PATCH /v1/print-signers/:id` — Update print signer
- `POST /v1/print-signers/all` — Get All Print Signers
- `POST /v1/print-signers/{id}` — Delete Print Signers
- `POST /v1/print-signers/{id}` — Get Print Signer By Id

## Printer
- `GET /v1/print-multi/{table_name}/{id}` — Print Document
    - body: table_name ((required)), template ((optional)), lang ((optional))
- `GET /v1/print/data` — Print Document
    - body: data_array ((required))
- `GET /v1/print/{table_name}/{id}` — Print Document
    - body: table_name ((required)), id ((required)), template ((optional)), lang ((optional))
- `GET /v1/print/{table_name}/{id}` — Print Document
    - body: table_name ((required)), id ((required)), template ((optional)), lang ((optional))
- `GET /v1/printable-documents/{table_name}/{id}` — Printable Documents
    - body: table_name ((required)), id ((required)), lang ((optional))
- `GET /v1/printers/[id]` — Get printer by id
- `GET /v1/printers/all` — Get printers
- `GET /v1/printers/auth` — Get printers
- `GET /v1/printers/{id}/send-document` — Send to printer
    - body: table_name ((required)), template ((optional)), lang ((optional))

## Processes
- `GET /v1/processes/available/:userId` — Get Available Processes
- `GET /v1/processes/start/` — Start Process
- `GET /v1/processes/start/` — Start Process
- `GET /v1/processes/tasks/` — User Tasks

## ProductDocumentation
- `GET /v1/product-documentation/:id` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/product-documentation/:id` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/product-documentation/:id` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/product-documentation/:id` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/product-documentation/:id` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/product-documentation/:id` — Endpoint title here..
    - body: parameters (here..)
- `PATCH /v1/product-documentation/:id` — Endpoint title here..
    - body: parameters (here..)

## Product_Line_Product
- `GET /v1/product-line-product` — Paginate Product Line Product
- `POST /v1/product-line-product` — Create Product Line Product
    - body: min_stock ((required)), max_stock ((required)), product_id ((required, exists:products.id)), product_line_id ((required, exists:product_lines.id)), warehouse_location_id ((required, exists:warehouse_locations.id))
- `DELETE /v1/product-line-product/:id` — Delete Product Line Product
- `GET /v1/product-line-product/:id` — Get Product Line Product
- `PATCH /v1/product-line-product/:id` — Update Product Line Product
    - body: min_stock ((required)), max_stock ((required)), product_id ((required, exists:products.id)), product_line_id ((required, exists:product_lines.id)), warehouse_location_id ((required, exists:warehouse_locations.id))
- `GET /v1/product-line-product/all` — Get All Product Line Product

## Product_Lines
- `GET /v1/product-lines` — Paginate Product Lines
- `POST /v1/product-lines` — Create Product Line
    - body: name ((optional)), default_warehouse_location_id ((optional, exists:warehouse_locations.id))
- `DELETE /v1/product-lines/:id` — Delete Product Line
- `GET /v1/product-lines/:id` — Get Product Line
- `PATCH /v1/product-lines/:id` — Update Product Line
    - body: name ((optional)), default_warehouse_location_id ((optional, exists:warehouse_locations.id))
- `GET /v1/product-lines/all` — Get All Product Lines

## Product_Types
- `GET /v1/product-tool-types` — Paginate Product Types
- `POST /v1/product-tool-types` — Create Product Type
    - body: name ((required, max:255)), slug ((required, max:255))
- `DELETE /v1/product-tool-types/:id` — Delete Product Type
- `GET /v1/product-tool-types/:id` — Get Product Type
- `PATCH /v1/product-tool-types/:id` — Update Product Type
    - body: name ((required, max:255)), slug ((required, max:255))
- `GET /v1/product-tool-types/all` — Get All Product Types
- `GET /v1/product-types` — Paginate Product Types
- `POST /v1/product-types` — Create Product Type
    - body: expense_event_id ((optional, exists:expense_events.id)), tax_rate_id ((optional, exists:tax_rates.id)), name ((required, max:255)), description ((optional)), use_in_bom ((optional)), use_in_sales ((optional)), use_in_purchasing ((optional)), use_in_purchasing_requirements ((optional)), use_in_material_requirements ((optional)), has_bom ((optional)), stock_tracking ((optional)), is_promo_writeoff ((optional))
- `DELETE /v1/product-types/:id` — Delete Product Type
- `GET /v1/product-types/:id` — Get Product Type
- `PATCH /v1/product-types/:id` — Update Product Type
    - body: expense_event_id ((optional, exists:expense_events.id)), tax_rate_id ((optional, exists:tax_rates.id)), name ((required, max:255)), description ((optional)), use_in_bom ((optional)), use_in_sales ((optional)), use_in_purchasing ((optional)), use_in_purchasing_requirements ((optional)), use_in_material_requirements ((optional)), has_bom ((optional)), stock_tracking ((optional)), is_promo_writeoff ((optional))
- `GET /v1/product-types/all` — Get All Product Types

## Production
- `GET /v1/production/add-order-sale-items-to-packing-work-order Add order sale item to` — packing work order
    - body: work_order_id ((required)), order_items ((required))
- `GET /v1/production/create-packing-work-order-for-sale-items Create packing work order for` — order items
    - body: order_items ((required))
- `GET /v1/production/create-work-order-from-packing-items` — Create work order from packing items
    - body: work_order_id ((required)), work_order_items ((optional))
- `GET /v1/production/orders` — Get production orders..
- `GET /v1/production/services` — Get production services..
- `GET /v1/production/services` — Get production services..
- `GET /v1/production/services` — Get production services..
- `GET /v1/production/services` — Get production services..
- `GET /v1/production/services` — Get production services..
- `GET /v1/production/services` — Get production services..
- `GET /v1/production/services` — Get production services..
- `GET /v1/production/services` — Get production services..
- `GET /v1/production/services` — Get production services..
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production
- `GET /v1/production/start` — Start production

## ProductionOperations
- `GET /v1/production-operations/cancel-material-delivery/{id}` — startProduction

## Products
- `GET /v1/price-list-products` — Get All Price List Products
- `GET /v1/products` — Paginate Products
- `POST /v1/products` — Create Product
    - body: tariff_code_id ((optional, exists:tariff_codes.id)), tariff_code_in_id ((optional, exists:tariff_codes.id)), tariff_code_out_id ((optional, exists:tariff_codes.id)), origin_country_id ((optional, alpha, max:2, min:2, exists:countries.id)), price_template_id ((optional, exists:price_templates.id)), product_type_id ((required, exists:product_types.id)), product_classification_id ((optinal, exists:product_classifications.id)), revision_owner_user_id ((optional)), tax_rate_id ((optional)), unit_id ((optional)), warehouse_location_id ((optional)), warehouse_location_receipt_id ((optional)), project_id ((optional)), parent_id ((optional)), sku ((required)), short_name ((required)), name ((required)), description ((optional)), weight ((required)), height ((optional)), widht ((optional)), lenght ((optional)), amount_internal ((optional)), amount_production ((optional)), amount_production_material ((optional)), amount_production_labour ((optional)), amount_packing_material ((optional)), amount_packing_labour ((optional)), ever_in_shop ((optional)), displayed_in_shop ((optional)), date_release ((optional)), stock_total ((optional)), stock_supply ((optional)), stock_available ((optional)), stock_in_delivery ((optional)), stock_in_production ((optional)), stock_supply_for_requirements ((optional)), required_for_orders ((optional)), required_for_work_orders ((optional)), stock_safety ((optional)), stock_maximum ((optional)), stock_for_orders ((optional)), stock_tracking ((optional)), stock_tracking_serial_numbers ((optional)), revision ((optional)), revision_number ((optional)), revision_release_date ((optional, format:Y-m-d H:i:s)), product_pic ((optional)), weight_plastic_package_avg ((optional)), weight_carton_package_avg ((optional)), date_out_of_stock ((optional)), date_first_order_out_of_stock ((optional)), stock_safety_set ((optional)), lifetime_warranty ((optional)), responsible_user_id ((optional)), product_box_id ((optional)), product_tool_type_id ((optional)), export_control_classification_number_id ((optional)), is_order_batch_production ((optional)), quantity_required ((optional)), quantity_required_production ((optional)), quantity_average_use ((optional)), quantity_minimum_batch ((optional)), date_first_incoming ((optional, format:Y-m-d H:i:s)), date_first_required ((optional, format:Y-m-d H:i:s)), skip_in_single_piece_flow ((optional)), product_line_id ((optional, exists:product_lines.id))
- `POST /v1/products` — Create Product
    - body: tariff_code_id ((optional, exists:tariff_codes.id)), tariff_code_in_id ((optional, exists:tariff_codes.id)), tariff_code_out_id ((optional, exists:tariff_codes.id)), origin_country_id ((optional, alpha, max:2, min:2, exists:countries.id)), price_template_id ((optional, exists:price_templates.id)), product_type_id ((required, exists:product_types.id)), product_classification_id ((optinal, exists:product_classifications.id)), revision_owner_user_id ((optional)), tax_rate_id ((optional)), unit_id ((optional)), warehouse_location_id ((optional)), warehouse_location_receipt_id ((optional)), project_id ((optional)), parent_id ((optional)), sku ((required)), short_name ((required)), name ((required)), description ((optional)), weight ((required)), height ((optional)), widht ((optional)), lenght ((optional)), amount_internal ((optional)), amount_production ((optional)), amount_production_material ((optional)), amount_production_labour ((optional)), amount_packing_material ((optional)), amount_packing_labour ((optional)), ever_in_shop ((optional)), displayed_in_shop ((optional)), date_release ((optional)), stock_total ((optional)), stock_supply ((optional)), stock_available ((optional)), stock_in_delivery ((optional)), stock_in_production ((optional)), stock_supply_for_requirements ((optional)), required_for_orders ((optional)), required_for_work_orders ((optional)), stock_safety ((optional)), stock_maximum ((optional)), stock_for_orders ((optional)), stock_tracking ((optional)), stock_tracking_serial_numbers ((optional)), revision ((optional)), revision_number ((optional)), revision_release_date ((optional, format:Y-m-d H:i:s)), product_pic ((optional)), weight_plastic_package_avg ((optional)), weight_carton_package_avg ((optional)), date_out_of_stock ((optional)), date_first_order_out_of_stock ((optional)), stock_safety_set ((optional)), lifetime_warranty ((optional)), responsible_user_id ((optional)), product_box_id ((optional)), product_tool_type_id ((optional)), export_control_classification_number_id ((optional)), is_order_batch_production ((optional)), quantity_required ((optional)), quantity_required_production ((optional)), quantity_average_use ((optional)), quantity_minimum_batch ((optional)), date_first_incoming ((optional, format:Y-m-d H:i:s)), date_first_required ((optional, format:Y-m-d H:i:s)), skip_in_single_piece_flow ((optional)), product_line_id ((optional, exists:product_lines.id))
- `DELETE /v1/products/:id` — Delete Product
- `GET /v1/products/:id` — Get Product
- `GET /v1/products/:id` — Get Product
- `GET /v1/products/:id` — Get Product
- `PATCH /v1/products/:id` — Update Product
    - body: tariff_code_id ((optional, exists:tariff_codes.id)), tariff_code_in_id ((optional, exists:tariff_codes.id)), tariff_code_out_id ((optional, exists:tariff_codes.id)), origin_country_id ((optional, alpha, max:2, min:2, exists:countries.id)), price_template_id ((optional, exists:price_templates.id)), product_type_id ((required, exists:product_types.id)), product_classification_id ((optinal, exists:product_classifications.id)), revision_owner_user_id ((optional)), tax_rate_id ((optional)), unit_id ((optional)), warehouse_location_id ((optional)), warehouse_location_receipt_id ((optional)), project_id ((optional)), parent_id ((optional)), sku ((required)), short_name ((required)), name ((required)), description ((optional)), weight ((required)), height ((optional)), widht ((optional)), lenght ((optional)), amount_internal ((optional)), amount_production ((optional)), amount_production_material ((optional)), amount_production_labour ((optional)), amount_packing_material ((optional)), amount_packing_labour ((optional)), ever_in_shop ((optional)), displayed_in_shop ((optional)), date_release ((optional)), stock_total ((optional)), stock_supply ((optional)), stock_available ((optional)), stock_in_delivery ((optional)), stock_in_production ((optional)), stock_supply_for_requirements ((optional)), required_for_orders ((optional)), required_for_work_orders ((optional)), stock_safety ((optional)), stock_maximum ((optional)), stock_for_orders ((optional)), stock_tracking ((optional)), stock_tracking_serial_numbers ((optional)), revision ((optional)), revision_number ((optional)), revision_release_date ((optional, format:Y-m-d H:i:s)), product_pic ((optional)), weight_plastic_package_avg ((optional)), weight_carton_package_avg ((optional)), date_out_of_stock ((optional)), date_first_order_out_of_stock ((optional)), stock_safety_set ((optional)), lifetime_warranty ((optional)), responsible_user_id ((optional)), product_box_id ((optional)), product_tool_type_id ((optional)), export_control_classification_number_id ((optional)), is_order_batch_production ((optional)), quantity_required ((optional)), quantity_required_production ((optional)), quantity_average_use ((optional)), quantity_minimum_batch ((optional)), date_first_incoming ((optional, format:Y-m-d H:i:s)), date_first_required ((optional, format:Y-m-d H:i:s)), skip_in_single_piece_flow ((optional)), product_line_id ((optional, exists:product_lines.id))
- `PATCH /v1/products/:id` — Update Product
    - body: tariff_code_id ((optional, exists:tariff_codes.id)), tariff_code_in_id ((optional, exists:tariff_codes.id)), tariff_code_out_id ((optional, exists:tariff_codes.id)), origin_country_id ((optional, alpha, max:2, min:2, exists:countries.id)), price_template_id ((optional, exists:price_templates.id)), product_type_id ((required, exists:product_types.id)), product_classification_id ((optinal, exists:product_classifications.id)), revision_owner_user_id ((optional)), tax_rate_id ((optional)), unit_id ((optional)), warehouse_location_id ((optional)), warehouse_location_receipt_id ((optional)), project_id ((optional)), parent_id ((optional)), sku ((required)), short_name ((required)), name ((required)), description ((optional)), weight ((required)), height ((optional)), widht ((optional)), lenght ((optional)), amount_internal ((optional)), amount_production ((optional)), amount_production_material ((optional)), amount_production_labour ((optional)), amount_packing_material ((optional)), amount_packing_labour ((optional)), ever_in_shop ((optional)), displayed_in_shop ((optional)), date_release ((optional)), stock_total ((optional)), stock_supply ((optional)), stock_available ((optional)), stock_in_delivery ((optional)), stock_in_production ((optional)), stock_supply_for_requirements ((optional)), required_for_orders ((optional)), required_for_work_orders ((optional)), stock_safety ((optional)), stock_maximum ((optional)), stock_for_orders ((optional)), stock_tracking ((optional)), stock_tracking_serial_numbers ((optional)), revision ((optional)), revision_number ((optional)), revision_release_date ((optional, format:Y-m-d H:i:s)), product_pic ((optional)), weight_plastic_package_avg ((optional)), weight_carton_package_avg ((optional)), date_out_of_stock ((optional)), date_first_order_out_of_stock ((optional)), stock_safety_set ((optional)), lifetime_warranty ((optional)), responsible_user_id ((optional)), product_box_id ((optional)), product_tool_type_id ((optional)), export_control_classification_number_id ((optional)), is_order_batch_production ((optional)), quantity_required ((optional)), quantity_required_production ((optional)), quantity_average_use ((optional)), quantity_minimum_batch ((optional)), date_first_incoming ((optional, format:Y-m-d H:i:s)), date_first_required ((optional, format:Y-m-d H:i:s)), skip_in_single_piece_flow ((optional)), product_line_id ((optional, exists:product_lines.id))
- `PATCH /v1/products/:id/add-to-price-list-version` — Add to price list version
    - body: price_list_version_id ((required)), amount ((required))
- `PATCH /v1/products/:id/add-to-price-list-version` — Add to price list version
    - body: price_list_version_id ((required)), amount ((required))
- `DELETE /v1/products/:id/delete-product-serials-recursively` — Delete Product serials recursively
- `POST /v1/products/:id/recalculate-stock` — Recalculate Product stock
    - body: tariff_code_id ((optional, exists:tariff_codes.id)), tariff_code_in_id ((optional, exists:tariff_codes.id)), tariff_code_out_id ((optional, exists:tariff_codes.id)), origin_country_id ((optional, alpha, max:2, min:2, exists:countries.id)), price_template_id ((optional, exists:price_templates.id)), product_type_id ((required, exists:product_types.id)), product_classification_id ((optinal, exists:product_classifications.id)), revision_owner_user_id ((optional)), tax_rate_id ((optional)), unit_id ((optional)), warehouse_location_id ((optional)), warehouse_location_receipt_id ((optional)), project_id ((optional)), parent_id ((optional)), sku ((required)), short_name ((required)), name ((required)), description ((optional)), weight ((required)), height ((optional)), widht ((optional)), lenght ((optional)), amount_internal ((optional)), amount_production ((optional)), amount_production_material ((optional)), amount_production_labour ((optional)), amount_packing_material ((optional)), amount_packing_labour ((optional)), ever_in_shop ((optional)), displayed_in_shop ((optional)), date_release ((optional)), stock_total ((optional)), stock_supply ((optional)), stock_available ((optional)), stock_in_delivery ((optional)), stock_in_production ((optional)), stock_supply_for_requirements ((optional)), required_for_orders ((optional)), required_for_work_orders ((optional)), stock_safety ((optional)), stock_maximum ((optional)), stock_for_orders ((optional)), stock_tracking ((optional)), stock_tracking_serial_numbers ((optional)), revision ((optional)), revision_number ((optional)), revision_release_date ((optional, format:Y-m-d H:i:s)), product_pic ((optional)), weight_plastic_package_avg ((optional)), weight_carton_package_avg ((optional)), date_out_of_stock ((optional)), date_first_order_out_of_stock ((optional)), stock_safety_set ((optional)), lifetime_warranty ((optional)), responsible_user_id ((optional)), product_box_id ((optional)), product_tool_type_id ((optional)), export_control_classification_number_id ((optional)), is_order_batch_production ((optional)), quantity_required ((optional)), quantity_required_production ((optional)), quantity_average_use ((optional)), quantity_minimum_batch ((optional)), date_first_incoming ((optional, format:Y-m-d H:i:s)), date_first_required ((optional, format:Y-m-d H:i:s)), skip_in_single_piece_flow ((optional)), product_line_id ((optional, exists:product_lines.id))
- `GET /v1/products/:id/stock-by-location` — Get Product stock by locations
- `GET /v1/products/:id/stock-by-location-lot` — Get Product stock by locations and by lots
- `GET /v1/products/:id/stock-by-lot` — Get Product stock by lots
- `GET /v1/products/:id/stock-transactions` — Get Product stock transactions
- `GET /v1/products/all` — Get All Product
- `POST /v1/products/bulk-replace-bom-material` — Bulk replace bom material
    - body: product_id ((required)), material ((required)), product_bom_ids ((optional)), work_order_item_ids ((optional))
- `GET /v1/products/stats/{:specific_statistics?}` — Get Product stats
- `GET /v1/products/{:id|:sku}/locations/{:work-order-item-id|:work-order-item-number}` — Get Product available Locations
- `GET /v1/products/{:id|:sku}/locations/{:work-order-item-id|:work-order-item-number}` — Get Product available Locations

## Projects
- `GET /v1/projects` — Lists All Projects
- `POST /v1/projects` — Create Project
    - body: name ((required, max:255)), description ((optional))
- `DELETE /v1/projects/:id` — Delete Project
- `GET /v1/projects/:id` — Get Project
- `PATCH /v1/projects/:id` — Update Project
    - body: name ((required, max:255)), description ((optional))
- `GET /v1/projects/all` — Get all Projects

## Queue
- `GET /v1/queue` — Get user's jobs...
- `DELETE /v1/queue/:id` — Cancel a job
    - body: parameters (here.)
- `PATCH /v1/queue/:id` — Retry job
    - body: parameters (here..)
- `PATCH /v1/queue/:id` — Retry job
    - body: parameters (here..)
- `GET /v1/queue/dispatch-dummy` — dispatchDummyJob
    - body: parameters (here..)
- `GET /v1/queue/dispatch-dummy` — dispatchDummyJob
    - body: parameters (here..)

## Regions
- `GET /v1/regions` — Paginate Regions
- `POST /v1/regions` — Create Region
    - body: name ((required, max:255)), description ((optional))
- `DELETE /v1/regions/:id` — Delete Region
- `GET /v1/regions/:id` — Get Region
- `PATCH /v1/regions/:id` — Update Region
    - body: name ((required, max:255)), description ((optional))
- `GET /v1/regions/all` — Get All Regions

## ResourceTypes
- `GET /v1/resource_types` — Paginate ResourceTypes
- `POST /v1/resource_types` — Create ResourceType
    - body: partner_id ((optional)), name ((required)), description ((optional))
- `DELETE /v1/resource_types/:id` — Delete ResourceType
- `GET /v1/resource_types/:id` — Get ResourceType
- `PATCH /v1/resource_types/:id` — Update ResourceType
    - body: partner_id ((optional)), name ((required)), description ((optional))
- `GET /v1/resource_types/all` — Get All ResourceTypes

## Resources
- `GET /v1/resources` — Paginate Resources
- `POST /v1/resources` — Create Resource
    - body: name ((required)), description ((required)), daily_capacity ((optional)), resource_type_id ((required, exists:resource_types.id)), active ((optional)), active_on_weekends ((optional)), active_on_holidays ((optional)), time_start ((optional, format:H:i:s)), efficiency ((optional)), console_uid ((optional)), can_manufacture_all_products ((optional))
- `DELETE /v1/resources/:id` — Delete Resource
- `GET /v1/resources/:id` — Get Resource
- `PATCH /v1/resources/:id` — Update Resource
    - body: name ((required)), description ((required)), daily_capacity ((optional)), resource_type_id ((required, exists:resource_types.id)), active ((optional)), active_on_weekends ((optional)), active_on_holidays ((optional)), time_start ((optional, format:H:i:s)), efficiency ((optional)), console_uid ((optional)), can_manufacture_all_products ((optional))
- `GET /v1/resources/all` — Get All Resources
- `POST /v1/resources/{id}/link-to-products` — Link resource to products

## RewardsAndBonuses
- `GET /v1/rewards-and-bonuses` — Lists All Rewards And Bonuses
- `POST /v1/rewards-and-bonuses` — Create New Rewards And Bonuses
- `PATCH /v1/rewards-and-bonuses/:id` — Update Rewards And Bonuses
- `POST /v1/rewards-and-bonuses/all` — Get All Rewards And Bonuses
- `GET /v1/rewards-and-bonuses/list-users` — Lists All Users That Current User Can Give A Reward To.
- `POST /v1/rewards-and-bonuses/{id}` — Delete Rewards And Bonuses
- `POST /v1/rewards-and-bonuses/{user_id}` — Get Rewards And Bonuses By Id

## Roles
- `GET /v1/roles` — List paginated Roles
- `POST /v1/roles` — Create a Role
    - body: name ((required, unique:roles, name, no_spaces)), guard_name ((required, in:api.web)), display_name ((required)), description ((optional)), level ((required))
- `DELETE /v1/roles/:id` — Delete a Role
- `GET /v1/roles/:id` — Find a Role by ID
- `PATCH /v1/roles/:id` — Update Role
    - body: name ((required, unique:roles, name, no_spaces)), guard_name ((required, in:api.web)), display_name ((required)), description ((optional)), level ((required))
- `GET /v1/roles/all` — Paginate Roles

## Sale_Types
- `GET /v1/sale-types` — Paginate Sale Types
- `POST /v1/sale-types` — Create Sale Type
    - body: name ((required, max:255)), code ((optional))
- `DELETE /v1/sale-types/:id` — Delete Sale Type
- `GET /v1/sale-types/:id` — Get Sale Type
- `PATCH /v1/sale-types/:id` — Update Sale Type
    - body: name ((required, max:255)), code ((optional))
- `GET /v1/sale-types/all` — Get All Sale Types

## SalesForecast
- `GET /v1/sales-forecasts/:id` — Get SalesForecast

## SalesForecastAdjustments
- `GET /v1/sales-forecast-adjustments` — Lists All SalesForecastAdjustments
- `POST /v1/sales-forecast-adjustments` — Create SalesForecastAdjustment
    - body: comment ((required)), sales_forecast_id ((required, exists:sales_forecasts.id)), amount_total ((optional)), date_approved ((optional, format:Y-m-d H:i:s)), date_rejected ((optional, format:Y-m-d H:i:s)), rejection_comment ((optional)), approver_user_id ((optional, exists:users.id))
- `DELETE /v1/sales-forecast-adjustments/:id` — Delete SalesForecastAdjustment
- `GET /v1/sales-forecast-adjustments/:id` — Get SalesForecastAdjustment
- `GET /v1/sales-forecast-adjustments/all` — Get all SalesForecastAdjustments

## SalesForecastAdjustmentss
- `PATCH /v1/salesforecastadjustments/:id` — Update SalesForecastAdjustments
    - body: comment ((required)), sales_forecast_id ((required, exists:sales_forecasts.id)), amount_total ((optional)), date_approved ((optional, format:Y-m-d H:i:s)), date_rejected ((optional, format:Y-m-d H:i:s)), rejection_comment ((optional)), approver_user_id ((optional, exists:users.id))

## SalesForecasts
- `GET /v1/get-order-product-quantities` — Get order product quantities for forecast
- `POST /v1/sales-forecasts-historical` — Create SalesForecast
    - body: partner_id ((required, exists:partners.id)), document_type_id ((optional, exists:document_types.id)), document_number ((optional, max:255)), date_from ((optional, format:Y-m-d H:i:s)), date_to ((optional, format:Y-m-d H:i:s)), period ((optional, max:255)), amount_total ((optional)), amount_total_rolling ((optional)), amount_total_actual ((optional))
- `POST /v1/sales-forecasts-parent-based` — Create SalesForecast
    - body: partner_id ((required, exists:partners.id)), document_type_id ((optional, exists:document_types.id)), document_number ((optional, max:255)), date_from ((optional, format:Y-m-d H:i:s)), date_to ((optional, format:Y-m-d H:i:s)), period ((optional, max:255)), amount_total ((optional)), amount_total_rolling ((optional)), amount_total_actual ((optional))
- `POST /v1/sales-forecasts/:id/` — GenerateWorkOrdersForForecast
    - body: partner_id ((required, exists:partners.id)), document_type_id ((optional, exists:document_types.id)), document_number ((optional, max:255)), date_from ((optional, format:Y-m-d H:i:s)), date_to ((optional, format:Y-m-d H:i:s)), period ((optional, max:255)), amount_total ((optional)), amount_total_rolling ((optional)), amount_total_actual ((optional))
- `GET /v1/sales-forecasts/:id/analysis` — Get SalesForecastAnalysis
- `GET /v1/sales-forecasts/:id/children-analysis` — Get SalesForecastChildrenAnalysis

## Sales_forecast
- `POST /v1/tag-tree-with-sales` — getTagTreeWithSales

## Sales_forecast_items
- `GET /v1/sales-forecast-items/:id` — Get Sales forecast item products

## Scheduled_jobs
- `GET /v1/scheduled-jobs` — Paginate Scheduled jobs
- `POST /v1/scheduled-jobs` — Create Schedule job
- `DELETE /v1/scheduled-jobs/:id` — Delete Scheduled jobs
- `GET /v1/scheduled-jobs/:id` — Get Scheduled jobs
- `PATCH /v1/scheduled-jobs/:id` — Update Scheduled jobs
    - body: name ((required)), slug ((optional)), description ((optional)), cron_interval ((optional)), cron_time ((optional)), command ((required)), notify_on_fail ((optional)), enabled ((optional))
- `PATCH /v1/scheduled-jobs/:id` — Update Scheduled jobs
    - body: name ((required)), slug ((optional)), description ((optional)), cron_interval ((optional)), cron_time ((optional)), command ((required)), notify_on_fail ((optional)), enabled ((optional))
- `GET /v1/scheduled-jobs/all` — Get All Scheduled jobs

## Serial_BOMs
- `GET /v1/serial-bom` — Paginate Serial BOM
- `POST /v1/serial-bom` — Create Serial BOM
    - body: serial_id ((required, exists:serials.id)), product_id ((required, exists:products.id)), work_order_item_id ((required, exists:work_order_items.id)), quantity ((required, min:0.0001)), quantity_used ((optional)), quantity_virtual_reservation ((optional)), quantity_physical_reservation ((optional))
- `DELETE /v1/serial-bom/:id` — Delete Serial BOM
- `GET /v1/serial-bom/:id` — Get Serial BOM
- `PATCH /v1/serial-bom/:id` — Update Serial BOM
    - body: serial_id ((required, exists:serials.id)), product_id ((required, exists:products.id)), work_order_item_id ((required, exists:work_order_items.id)), quantity ((required, min:0.0001)), quantity_used ((optional)), quantity_virtual_reservation ((optional)), quantity_physical_reservation ((optional))
- `PATCH /v1/serial-bom/:id/attach-serial` — Update Serial BOM
    - body: serials ((optional)), quantity ((optional))
- `POST /v1/serial-bom/:id/restock` — Restock Serial BOM Serial
- `PATCH /v1/serial-bom/:id/set-used` — Update Serial BOM
    - body: serials ((optional)), quantity ((optional))
- `POST /v1/serial-bom/:id/virtual-reservation` — Virtual reserve serail bom material
    - body: quantity ((optional))
- `DELETE /v1/serial-bom/:serialBomId/:serialId` — Delete Serial BOM Serial
- `POST /v1/serial-bom/:serialBomId/:serialId/restock` — Restock Serial BOM Serial
- `PATCH /v1/serial-bom/:serialBomId/:serialId/restore` — Restore Serial BOM Serial
- `GET /v1/serial-bom/all` — Get All Serial BOMs
- `PATCH /v1/serial-bom/batch-set-used` — Update Serial BOM
    - body: serials ((optional)), quantity ((optional))

## Serial_Calibrations
- `GET /v1/serial-calibrations` — Paginate Serial Calibrations
- `POST /v1/serial-calibrations` — Create Serial Calibrations
    - body: serial_id ((required, exists:serials.id)), user_id ((optional, exists:users.id)), username ((optional, max:255)), type ((optional, in:Adjustment, Report)), xml_file ((optional)), pdf ((optional)), certificate_number ((optional))
- `DELETE /v1/serial-calibrations/:id` — Delete Serial Calibrations
- `GET /v1/serial-calibrations/:id` — Get Serial Calibrations
- `PATCH /v1/serial-calibrations/:id` — Update Serial Calibrations
    - body: serial_id ((required, exists:serials.id)), user_id ((optional, exists:users.id)), username ((optional, max:255)), type ((optional, in:Adjustment, Report)), xml_file ((optional)), pdf ((optional)), certificate_number ((optional))
- `GET /v1/serial-calibrations/all` — Get All Serial Calibrations

## Serial_Fields
- `GET /v1/serial-fields` — Paginate Serial Fields
- `POST /v1/serial-fields` — Create Serial Fields
    - body: serial_id ((required, exists:serials.id)), name ((optional, max:255)), value ((optional)), visible ((optional))
- `DELETE /v1/serial-fields/:id` — Delete Serial Fields
- `GET /v1/serial-fields/:id` — Get Serial Fields
- `PATCH /v1/serial-fields/:id` — Update Serial Fields
    - body: serial_id ((required, exists:serials.id)), name ((optional, max:255)), value ((optional)), visible ((optional))
- `GET /v1/serial-fields/all` — Get All Serial Fields

## Serials
- `GET /v1/serials` — Paginate Serials
- `POST /v1/serials` — Create Serials
    - body: parent_id ((optional, exists:serials.id)), product_id ((optional, exists:products.id)), partner_id ((optional, exists:partners.id)), ds_license_id ((optional, exists:ds_licenses.id)), work_order_item_id ((optional, exists:work_order_items.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), lot_id ((optional, exists:lots.id)), serial_number ((required, max:255)), inventory_number ((optional, max:255)), demo ((optional)), rentable ((optional)), total_care_warranty ((optional)), to_be_defined ((optional)), date_sale ((optional, format:Y-m-d H:i:s)), date_last_calibration ((optional, format:Y-m-d H:i:s)), date_next_calibration ((optional, format:Y-m-d H:i:s)), date_warranty_due ((optional, format:Y-m-d H:i:s)), calibration_interval ((optional)), calibration_required_for_warranty ((optional)), warranty ((optional)), calibration_tray_prepared_by_id ((optional))
- `DELETE /v1/serials/:id` — Delete Serials
- `DELETE /v1/serials/:id` — Delete Serials
- `DELETE /v1/serials/:id` — Delete Serials
- `GET /v1/serials/:id` — Get Serials
- `GET /v1/serials/:id` — Get Serials
- `PATCH /v1/serials/:id` — Update Serials
    - body: parent_id ((optional, exists:serials.id)), product_id ((optional, exists:products.id)), partner_id ((optional, exists:partners.id)), ds_license_id ((optional, exists:ds_licenses.id)), work_order_item_id ((optional, exists:work_order_items.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), lot_id ((optional, exists:lots.id)), serial_number ((required, max:255)), inventory_number ((optional, max:255)), demo ((optional)), rentable ((optional)), total_care_warranty ((optional)), to_be_defined ((optional)), date_sale ((optional, format:Y-m-d H:i:s)), date_last_calibration ((optional, format:Y-m-d H:i:s)), date_next_calibration ((optional, format:Y-m-d H:i:s)), date_warranty_due ((optional, format:Y-m-d H:i:s)), calibration_interval ((optional)), calibration_required_for_warranty ((optional)), warranty ((optional)), calibration_tray_prepared_by_id ((optional))
- `GET /v1/serials/:id/calibration-report` — Get Serial calibration report
- `GET /v1/serials/:id/calibration-report` — Get Serial calibration report
- `GET /v1/serials/:id/calibration-report-recursive-xml` — Get Serial calibration recursive xml
- `GET /v1/serials/:id/generate-tds-license` — Generate TDS license
- `GET /v1/serials/:id/stock-transactions` — Get Serial stock transactions
- `POST /v1/serials/:id/virtual-reservation` — Virtual reserve serail material
- `POST /v1/serials/:id/virtual-reservation` — Virtual reserve serail material
- `GET /v1/serials/all` — Get All Serials
- `POST /v1/serials/{serial_id}/bom` — Create Serial BOM
    - body: serial_id ((required, exists:serials.id)), product_id ((required, exists:products.id)), work_order_item_id ((required, exists:work_order_items.id)), quantity ((required, min:0.0001)), quantity_used ((optional)), quantity_virtual_reservation ((optional)), quantity_physical_reservation ((optional))

## Service_Errors
- `GET /v1/service-errors` — Paginate Service Errors
- `POST /v1/service-errors` — Create ServiceError
    - body: name ((required, max:255)), description ((optional))
- `DELETE /v1/service-errors/:id` — Delete Service Service Errors
- `GET /v1/service-errors/:id` — Get Service Errors
- `PATCH /v1/service-errors/:id` — Update Service Errors
    - body: name ((required, max:255)), description ((optional))
- `GET /v1/service-errors/all` — Get All Service Service Errors

## Service_Externals
- `GET /v1/services-external` — Paginate Service Externals
- `POST /v1/services-external` — Create ServiceExternal
    - body: order_sale_item_id ((optional, exists:order_sale_items.id)), serial_id ((optional, exists:serials.id)), handling_country_id ((required, exists:countries.id)), document_type_id ((optional, exists:document_types.id)), document_number ((optional, max:255)), reference_number ((optional, max:255)), external_reference_number ((optional, max:255)), service_report_number ((optional, max:32)), customer_error_description ((optional)), request_firmware_update ((optional)), service_team_coordinator_user_id ((optional, exists:users.id)), service_package_description ((optional)), service_root_cause_analyses_due_date ((optional, format:Y-m-d H:i:s)), service_corrective_actions ((optional)), service_corrective_actions_due_date ((optional, format:Y-m-d H:i:s)), service_validated_actions ((optional)), service_validated_actions_responsible_user_id ((optional, exists:users.id)), service_implemented_actions ((optional)), service_implemented_actions_responsible_user_id ((optional, exists:users.id)), defect_cause_description ((optional)), error_prevention_description ((optional)), firmware_update ((optional)), calibration ((optional)), service_type_repair ((optional)), service_type_upgrade ((optional)), service_type_recalibration ((optional)), service_type_none ((optional)), service_team_recognition ((optional)), service_note ((optional)), service_time ((optional)), warranty ((optional)), date_received ((optional, format:Y-m-d H:i:s)), date_shipped ((optional, format:Y-m-d H:i:s)), date_closed ((optional, format:Y-m-d H:i:s)), date_estimated_amount_confirmed ((optional, format:Y-m-d H:i:sl)), estimated_amount_confirmed ((optional)), currency_code_id ((optional, alpha, exists:currency_codes.id)), amount_estimated_currency ((required)), service_box_number ((optional)), date_wanted ((optional, format:Y-m-d H:i:s))
- `POST /v1/services-external` — Create ServiceExternal
    - body: order_sale_item_id ((optional, exists:order_sale_items.id)), serial_id ((optional, exists:serials.id)), handling_country_id ((required, exists:countries.id)), document_type_id ((optional, exists:document_types.id)), document_number ((optional, max:255)), reference_number ((optional, max:255)), external_reference_number ((optional, max:255)), service_report_number ((optional, max:32)), customer_error_description ((optional)), request_firmware_update ((optional)), service_team_coordinator_user_id ((optional, exists:users.id)), service_package_description ((optional)), service_root_cause_analyses_due_date ((optional, format:Y-m-d H:i:s)), service_corrective_actions ((optional)), service_corrective_actions_due_date ((optional, format:Y-m-d H:i:s)), service_validated_actions ((optional)), service_validated_actions_responsible_user_id ((optional, exists:users.id)), service_implemented_actions ((optional)), service_implemented_actions_responsible_user_id ((optional, exists:users.id)), defect_cause_description ((optional)), error_prevention_description ((optional)), firmware_update ((optional)), calibration ((optional)), service_type_repair ((optional)), service_type_upgrade ((optional)), service_type_recalibration ((optional)), service_type_none ((optional)), service_team_recognition ((optional)), service_note ((optional)), service_time ((optional)), warranty ((optional)), date_received ((optional, format:Y-m-d H:i:s)), date_shipped ((optional, format:Y-m-d H:i:s)), date_closed ((optional, format:Y-m-d H:i:s)), date_estimated_amount_confirmed ((optional, format:Y-m-d H:i:sl)), estimated_amount_confirmed ((optional)), currency_code_id ((optional, alpha, exists:currency_codes.id)), amount_estimated_currency ((required)), service_box_number ((optional)), date_wanted ((optional, format:Y-m-d H:i:s))
- `DELETE /v1/services-external/:id` — Delete Service Service Externals
- `GET /v1/services-external/:id` — Get Service Externals
- `PATCH /v1/services-external/:id` — Update Service Externals
    - body: order_sale_item_id ((optional, exists:order_sale_items.id)), serial_id ((optional, exists:serials.id)), handling_country_id ((required, exists:countries.id)), document_type_id ((optional, exists:document_types.id)), document_number ((optional, max:255)), reference_number ((optional, max:255)), external_reference_number ((optional, max:255)), service_report_number ((optional, max:32)), customer_error_description ((optional)), request_firmware_update ((optional)), service_team_coordinator_user_id ((optional, exists:users.id)), service_package_description ((optional)), service_root_cause_analyses_due_date ((optional, format:Y-m-d H:i:s)), service_corrective_actions ((optional)), service_corrective_actions_due_date ((optional, format:Y-m-d H:i:s)), service_validated_actions ((optional)), service_validated_actions_responsible_user_id ((optional, exists:users.id)), service_implemented_actions ((optional)), service_implemented_actions_responsible_user_id ((optional, exists:users.id)), defect_cause_description ((optional)), error_prevention_description ((optional)), firmware_update ((optional)), calibration ((optional)), service_type_repair ((optional)), service_type_upgrade ((optional)), service_type_recalibration ((optional)), service_type_none ((optional)), service_team_recognition ((optional)), service_note ((optional)), service_time ((optional)), warranty ((optional)), date_received ((optional, format:Y-m-d H:i:s)), date_shipped ((optional, format:Y-m-d H:i:s)), date_closed ((optional, format:Y-m-d H:i:s)), date_estimated_amount_confirmed ((optional, format:Y-m-d H:i:sl)), estimated_amount_confirmed ((optional)), currency_code_id ((optional, alpha, exists:currency_codes.id)), amount_estimated_currency ((required)), service_box_number ((optional)), date_wanted ((optional, format:Y-m-d H:i:s))
- `PATCH /v1/services-external/:id` — Update Service Externals
    - body: order_sale_item_id ((optional, exists:order_sale_items.id)), serial_id ((optional, exists:serials.id)), handling_country_id ((required, exists:countries.id)), document_type_id ((optional, exists:document_types.id)), document_number ((optional, max:255)), reference_number ((optional, max:255)), external_reference_number ((optional, max:255)), service_report_number ((optional, max:32)), customer_error_description ((optional)), request_firmware_update ((optional)), service_team_coordinator_user_id ((optional, exists:users.id)), service_package_description ((optional)), service_root_cause_analyses_due_date ((optional, format:Y-m-d H:i:s)), service_corrective_actions ((optional)), service_corrective_actions_due_date ((optional, format:Y-m-d H:i:s)), service_validated_actions ((optional)), service_validated_actions_responsible_user_id ((optional, exists:users.id)), service_implemented_actions ((optional)), service_implemented_actions_responsible_user_id ((optional, exists:users.id)), defect_cause_description ((optional)), error_prevention_description ((optional)), firmware_update ((optional)), calibration ((optional)), service_type_repair ((optional)), service_type_upgrade ((optional)), service_type_recalibration ((optional)), service_type_none ((optional)), service_team_recognition ((optional)), service_note ((optional)), service_time ((optional)), warranty ((optional)), date_received ((optional, format:Y-m-d H:i:s)), date_shipped ((optional, format:Y-m-d H:i:s)), date_closed ((optional, format:Y-m-d H:i:s)), date_estimated_amount_confirmed ((optional, format:Y-m-d H:i:sl)), estimated_amount_confirmed ((optional)), currency_code_id ((optional, alpha, exists:currency_codes.id)), amount_estimated_currency ((required)), service_box_number ((optional)), date_wanted ((optional, format:Y-m-d H:i:s))
- `GET /v1/services-external/all` — Get All Service Service Externals

## Service_Internals
- `GET /v1/services-internal` — Paginate Service Internals
- `POST /v1/services-internal` — Create Service Internals
    - body: user_id ((required, exists:users.id)), serial_id ((optional, exists:serials.id)), document_type_id ((optional, exists:document_types.id)), document_number ((optional, max:255)), service_report_number ((optional, max:255)), reference_number ((optional, max:255)), error_description ((optional)), away_company ((optional)), date_away_due ((optional, format:Y-m-d H:i:s)), service_team_coordinator_user_id ((optional)), service_root_cause_analyses_due_date ((optional, format:Y-m-d H:i:s)), service_corrective_actions ((optional, exists:users.id)), service_corrective_actions_due_date ((optional, format:Y-m-d H:i:s)), service_validated_actions ((optional)), service_validated_actions_responsible_user_id ((optional, exists:users.id)), service_implemented_actions ((optional)), service_implemented_actions_responsible_user_id ((optional, exists:users.id)), defect_cause_description ((optional)), error_prevention_description ((optional)), firmware_update ((optional)), calibration ((optional)), service_type_repair ((optional)), service_type_upgrade ((optional)), service_type_recalibration ((optional)), service_team_recognition ((optional)), service_type_none ((optional)), date_closed ((optional, format:Y-m-d H:i:s))
- `DELETE /v1/services-internal/:id` — Delete Service Service Internals
- `GET /v1/services-internal/:id` — Get Service Service Internals
- `PATCH /v1/services-internal/:id` — Update Service Service Internals
    - body: user_id ((required, exists:users.id)), serial_id ((optional, exists:serials.id)), document_type_id ((optional, exists:document_types.id)), document_number ((optional, max:255)), service_report_number ((optional, max:255)), reference_number ((optional, max:255)), error_description ((optional)), away_company ((optional)), date_away_due ((optional, format:Y-m-d H:i:s)), service_team_coordinator_user_id ((optional)), service_root_cause_analyses_due_date ((optional, format:Y-m-d H:i:s)), service_corrective_actions ((optional, exists:users.id)), service_corrective_actions_due_date ((optional, format:Y-m-d H:i:s)), service_validated_actions ((optional)), service_validated_actions_responsible_user_id ((optional, exists:users.id)), service_implemented_actions ((optional)), service_implemented_actions_responsible_user_id ((optional, exists:users.id)), defect_cause_description ((optional)), error_prevention_description ((optional)), firmware_update ((optional)), calibration ((optional)), service_type_repair ((optional)), service_type_upgrade ((optional)), service_type_recalibration ((optional)), service_team_recognition ((optional)), service_type_none ((optional)), date_closed ((optional, format:Y-m-d H:i:s))
- `GET /v1/services-internal/:id/start-process` — Start error in production process
- `GET /v1/services-internal/all` — Get All Service Service Internals

## Shipping_Lists
- `GET /v1/shipping-lists` — Paginate Shipping Lists
- `POST /v1/shipping-lists` — Create Shipping Lists
    - body: partner_id ((required)), incoterm_id ((optional)), document_type_id ((required)), document_number ((required)), tracking_number ((optional)), package_count ((optional)), net_weight ((optional)), gross_weight ((optional)), print_footer ((optional))
- `DELETE /v1/shipping-lists/:id` — Delete Shipping Lists
- `GET /v1/shipping-lists/:id` — Get Shipping Lists
- `PATCH /v1/shipping-lists/:id` — Update Shipping Lists
    - body: partner_id ((required)), incoterm_id ((optional)), document_type_id ((required)), document_number ((required)), tracking_number ((optional)), package_count ((optional)), net_weight ((optional)), gross_weight ((optional)), print_footer ((optional))
- `GET /v1/shipping-lists/all` — Get All Shipping Lists
- `POST /v1/shipping-lists/create-parcel` — Create Parcel
    - body: shipping_list_id ((required))
- `POST /v1/shipping-lists/create-parcel` — Create Parcel
    - body: shipping_list_id ((required))
- `POST /v1/shipping-lists/create-parcel` — Create Parcel
    - body: shipping_list_id ((required))
- `POST /v1/shipping-lists/print-parcel` — Print Parcel
    - body: shipping_list_id ((required))

## Shipping_Methods
- `GET /v1/shipping-methods` — Paginate Shipping Methods
- `POST /v1/shipping-methods` — Create Shipping Method
    - body: partner_id ((optional)), incoterm_id ((optional)), name ((required)), description ((optional)), cost_calculation ((optional))
- `DELETE /v1/shipping-methods/:id` — Delete Shipping Method
- `GET /v1/shipping-methods/:id` — Get Shipping Method
- `PATCH /v1/shipping-methods/:id` — Update Shipping Methods
    - body: partner_id ((optional)), incoterm_id ((optional)), name ((required)), description ((optional)), cost_calculation ((optional))
- `GET /v1/shipping-methods/all` — Get All Shipping Methods

## Single_piece_flow_models
- `GET /v1/single-piece-flow-models` — Index Single piece flow model
- `POST /v1/single-piece-flow-models` — Create Single piece flow model
    - body: task_id ((optional, exists:tasks.id)), work_order_item_id ((required, exists:work_order_items.id)), serial_box_id ((optional, exists:serials.id)), serial_tray_id ((optional, exists:serials.id)), slot ((optional)), date_finished ((optional, format:Y-m-d H:i:s))
- `DELETE /v1/single-piece-flow-models/:id` — Delete Single piece flow model
- `GET /v1/single-piece-flow-models/:id` — Get Single piece flow model
- `PATCH /v1/single-piece-flow-models/:id` — Update Single piece flow model
    - body: task_id ((optional, exists:tasks.id)), work_order_item_id ((required, exists:work_order_items.id)), serial_box_id ((optional, exists:serials.id)), serial_tray_id ((optional, exists:serials.id)), slot ((optional)), date_finished ((optional, format:Y-m-d H:i:s))
- `GET /v1/single-piece-flow-models/all` — Get Single piece flow model

## Skills
- `GET /v1/skills` — Paginate Skills
- `POST /v1/skills` — Create Skill
    - body: name ((required, max:255)), description ((required))
- `DELETE /v1/skills/:id` — Delete Skill
- `GET /v1/skills/:id` — Get Skill
- `PATCH /v1/skills/:id` — Update Skill
    - body: name ((required, max:255)), description ((required))
- `GET /v1/skills/all` — Get All Skills

## SolutionAreas
- `GET /v1/solution-areas` — Lists All Solution Areas
- `POST /v1/solution-areas` — Create Solution Area
    - body: parent_id ((optional, exists:solutions.id)), solution_area_id ((optional, exists:solution_areas.id)), name ((required, max:255)), description ((optional))
- `DELETE /v1/solution-areas/:id` — Delete Solution Area
- `GET /v1/solution-areas/:id` — Get Solution Area
- `PATCH /v1/solution-areas/:id` — Update Solution Area
    - body: parent_id ((optional, exists:solutions.id)), solution_area_id ((optional, exists:solution_areas.id)), name ((required, max:255)), description ((optional))
- `GET /v1/solution-areas/all` — Get all Solution Areas

## Solutions
- `GET /v1/solutions` — Lists All Solutions
- `POST /v1/solutions` — Create Solution
    - body: name ((required, max:255)), description ((optional))
- `DELETE /v1/solutions/:id` — Delete Solution
- `GET /v1/solutions/:id` — Get Solution
- `PATCH /v1/solutions/:id` — Update Solution
    - body: name ((required, max:255)), description ((optional))
- `GET /v1/solutions/all` — Get all Solutions

## States
- `GET /v1/states` — Paginate States
- `POST /v1/states` — Create State
    - body: name ((required, max:255))
- `GET /v1/states-public` — Index States public
- `GET /v1/states-public/all` — Get All States public
- `DELETE /v1/states/:id` — Delete State
- `GET /v1/states/:id` — Get State
- `PATCH /v1/states/:id` — Update State
    - body: name ((required, max:255))
- `GET /v1/states/all` — Get All States

## Statistic
- `GET /v1/statistics/get-aging-by-partner/:date` — Get aging by partners
- `GET /v1/statistics/get-aging-by-supplier/:date` — Get aging by suppliers
- `GET /v1/statistics/get-inventory-report-revision-rows` — Get inventory report rows
- `GET /v1/statistics/get-inventory-report-revision/:date_from/:date_to` — Get inventory report..
    - body: parameters (here..)
- `GET /v1/statistics/get-inventory-report-rows` — Get inventory report rows
- `GET /v1/statistics/get-inventory-report/:date_from/:date_to` — Get inventory report..
    - body: parameters (here..)
- `GET /v1/statistics/get-invoice/:date` — Get invoice statistic
- `GET /v1/statistics/get-skv-customers/:date` — Get skv customers
- `GET /v1/statistics/get-skv-suppliers/:date` — Get skv suppliers
- `GET /v1/statistics/intrastat-in-report-details` — Get details for intrastat IN report
    - body: parameters (here..)
- `GET /v1/statistics/intrastat-in-report/:datefrom/:dateto` — Get inventory report..
    - body: parameters (here..)
- `GET /v1/statistics/intrastat-out-report/:datefrom/:dateto` — Get inventory report..
    - body: parameters (here..)
- `GET /v1/statistics/inventory-report/:datefrom/:dateto` — Get inventory report..
    - body: parameters (here..)
- `GET /v1/statistics/inventory-report/:datefrom/:dateto` — Get inventory report..
    - body: parameters (here..)
- `GET /v1/statistics/inventory-report/:datefrom/:dateto` — Get inventory report..
    - body: parameters (here..)
- `GET /v1/statistics/inventory-report/:datefrom/:dateto` — Get inventory report..
    - body: parameters (here..)
- `GET /v1/statistics/inventory-report/:datefrom/:dateto` — Get inventory report..
    - body: parameters (here..)
- `GET /v1/statistics/inventory-report/:datefrom/:dateto` — Get inventory report..
    - body: parameters (here..)
- `GET /v1/statistics/inventory-report/:datefrom/:dateto` — Get inventory report..
    - body: parameters (here..)
- `GET /v1/statistics/inventory-report/:datefrom/:dateto` — Get inventory report..
    - body: parameters (here..)
- `GET /v1/statistics/inventory-report/:datefrom/:dateto` — Get inventory report..
    - body: parameters (here..)
- `GET /v1/statistics/inventory-report/:datefrom/:dateto` — Get inventory report..
    - body: parameters (here..)
- `GET /v1/statistics/inventory-report/:datefrom/:dateto` — Get inventory report..
    - body: parameters (here..)
- `GET /v1/statistics/inventory-report/:datefrom/:dateto` — Get inventory report..
    - body: parameters (here..)
- `GET /v1/statistics/inventory-report/:datefrom/:dateto` — Get production report..
    - body: parameters (here..)
- `GET /v1/statistics/production-orders-current` — Get current production report..
- `GET /v1/statistics/reward-system/:year` — Reward system
    - body: parameters (here..)
- `GET /v1/statistics/reward-system/:year` — Reward system
    - body: parameters (here..)
- `GET /v1/statistics/stock-export/:date_to` — Export stock
    - body: parameters (here..)
- `GET /v1/statistics/stock-journal-export/:date_from/:date_to` — Export stock journal
    - body: parameters (here..)
- `PATCH /v1/statistics/update-amortization` — Update amortization
    - body: value ((required)), month ((required)), year ((required))
- `PATCH /v1/statistics/update-rentability` — Update rentability
    - body: value ((required)), month ((required)), year ((required))

## Status_Categories
- `GET /v1/status-categories` — Paginate Statuse Categories
- `POST /v1/status-categories` — Create Status Category
    - body: document_id ((required, exists:documents.id)), slug ((optional)), name ((required, max:255)), description ((optional)), default ((optional))
- `DELETE /v1/status-categories/:id` — Delete Status
- `GET /v1/status-categories/:id` — Get Status Category by ID
- `PATCH /v1/status-categories/:id` — Update Status Category
    - body: document_id ((required, exists:documents.id)), slug ((optional)), name ((required, max:255)), description ((optional)), default ((optional))
- `GET /v1/status-categories/all` — Get All Status Categories

## Statuses
- `GET /v1/statuses` — Paginate Statuses
- `POST /v1/statuses` — Create Status
    - body: name ((required, max:255)), description ((optional)), color ((optional)), font_style ((optional))
- `DELETE /v1/statuses/:id` — Delete Status
- `GET /v1/statuses/:id` — Get Status by ID
- `PATCH /v1/statuses/:id` — Update Status
    - body: name ((required, max:255)), description ((optional)), color ((optional)), font_style ((optional))
- `GET /v1/statuses/:table` — Get categorized statuses
- `GET /v1/statuses/:table` — Get statuses from table
- `GET /v1/statuses/:table` — Get statuses from table
- `GET /v1/statuses/:table` — Get statuses from table
- `GET /v1/statuses/all` — Get All Statuses
- `GET /v1/statuses/all` — Get All Statuses
- `GET /v1/statuses/all` — Get Status Throughput

## Stock_Adjustment_Items
- `GET /v1/stock-adjustment-items` — Lists All Stock Adjustment Items
- `POST /v1/stock-adjustment-items` — Create Stock Adjustment Item
    - body: stock_adjustment_id ((required, exists:stock_adjustments.id)), warehouse_location_id ((required, exists:warehouse_locations.id)), product_id ((required, exists:products.id)), lot_id ((required, exists:lots.id)), work_order_item_id ((optional, exists:work_order_items.id)), quantity ((required)), description ((optional))
- `DELETE /v1/stock-adjustment-items/:id` — Delete Stock Adjustment Item
- `GET /v1/stock-adjustment-items/:id` — Get Stock Adjustment Item
- `PATCH /v1/stock-adjustment-items/:id` — Update Stock Adjustment Items
    - body: stock_adjustment_id ((required, exists:stock_adjustments.id)), warehouse_location_id ((required, exists:warehouse_locations.id)), product_id ((required, exists:products.id)), lot_id ((required, exists:lots.id)), work_order_item_id ((optional, exists:work_order_items.id)), quantity ((required)), description ((optional))
- `GET /v1/stock-adjustment-items/all` — Get All Stock Adjustment Items

## Stock_Adjustments
- `GET /v1/stock-adjustments` — Lists All Stock Adjustments
- `POST /v1/stock-adjustments` — Create Stock Adjustment
    - body: stock_taking_id ((optional, exists:stock_takings.id)), document_type_id ((required, exists:document_types.id)), document_number ((optional, max:255)), date_booked ((optional)), date_transaction ((optional)), date_error ((optional)), error_description ((optional)), booked_by ((optional, exists:users.id))
- `POST /v1/stock-adjustments` — Create Stock Adjustment
    - body: stock_taking_id ((optional, exists:stock_takings.id)), document_type_id ((required, exists:document_types.id)), document_number ((optional, max:255)), date_booked ((optional)), date_transaction ((optional)), date_error ((optional)), error_description ((optional)), booked_by ((optional, exists:users.id))
- `DELETE /v1/stock-adjustments/:id` — Delete Stock Adjustment
- `GET /v1/stock-adjustments/:id` — Get Stock adjustments
- `PATCH /v1/stock-adjustments/:id` — Update Stock Adjustments
    - body: stock_taking_id ((optional, exists:stock_takings.id)), document_type_id ((required, exists:document_types.id)), document_number ((optional, max:255)), date_booked ((optional)), date_transaction ((optional)), date_error ((optional)), error_description ((optional)), booked_by ((optional, exists:users.id))
- `GET /v1/stock-adjustments/all` — Get All Stock Adjustments

## Stock_Bids
- `GET /v1/stock-bids` — Lists All Stock Bids
- `POST /v1/stock-bids` — Create Stock Bid
    - body: stock_id ((required, exists:stocks.id)), user_id ((optional, exists:users.id)), stocks ((required)), amount ((optional)), sell ((optional)), paid ((optional))
- `DELETE /v1/stock-bids/:id` — Delete Stock Bid
- `GET /v1/stock-bids/:id` — Get Stock Bids
- `PATCH /v1/stock-bids/:id` — Update Stock Bids
    - body: stock_id ((required, exists:stocks.id)), user_id ((optional, exists:users.id)), stocks ((required)), amount ((optional)), sell ((optional)), paid ((optional))
- `GET /v1/stock-bids/all` — Get All Stock Bids
- `GET /v1/stock-bids/all` — Get All Stock Bids
- `PATCH /v1/stock-bids/update-or-create-for-trading-window` — Bid

## Stock_Initial_Items
- `GET /v1/stock-initial-items` — Lists All Stock Initial Items
- `POST /v1/stock-initial-items` — Create Stock Initial Items
    - body: stock_initial_id ((required, exists:stock_initials.id)), warehouse_location_id ((required, exists:warehouse_locations.id)), product_id ((required, exists:products.id)), quantity ((required)), description ((optional))
- `DELETE /v1/stock-initial-items/:id` — Delete Stock Initial Item
- `GET /v1/stock-initial-items/:id` — Get Stock Initial Item
- `PATCH /v1/stock-initial-items/:id` — Update All Stock Initial Items
    - body: stock_initial_id ((required, exists:stock_initials.id)), warehouse_location_id ((required, exists:warehouse_locations.id)), product_id ((required, exists:products.id)), quantity ((required)), description ((optional))
- `GET /v1/stock-initial-items/all` — Get All Stock Initial Items

## Stock_Initials
- `GET /v1/stock-initials` — Lists All Stock Initials
- `POST /v1/stock-initials` — Create Stock Initial
    - body: stock_taking_id ((required, exists:stock_takings.id)), movement_type_id ((required, exists:movement_types.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), date_booked ((required))
- `POST /v1/stock-initials` — Create Stock Initials
    - body: stock_taking_id ((required, exists:stock_takings.id)), movement_type_id ((required, exists:movement_types.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), date_booked ((required))
- `DELETE /v1/stock-initials/:id` — Delete Stock Initial
- `GET /v1/stock-initials/:id` — Get Stock Initial
- `PATCH /v1/stock-initials/:id` — Update Stock Initials
    - body: stock_taking_id ((required, exists:stock_takings.id)), movement_type_id ((required, exists:movement_types.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), date_booked ((required))
- `GET /v1/stock-initials/:id/stock-transactions` — Get Stock Initial stock transactions
- `GET /v1/stock-initials/all` — Get All Stock Initials

## Stock_Taking_Report_Items
- `GET /v1/stock-taking-report-items` — Lists All Stock Taking Report Items
- `POST /v1/stock-taking-report-items` — Create Stock Taking Report Item
    - body: stock_taking_report_id ((required, exists:stock_taking_reports.id)), product_id ((required, exists:products.id)), work_order_id ((optional, exists:work_orders.id)), quantity1 ((required)), quantity2 ((optional)), serials1 ((optional)), serials1_new ((optional)), serials2 ((optional)), serials2_new ((optional)), system_serials ((optional)), system_quantity ((optional)), note ((optional))
- `DELETE /v1/stock-taking-report-items/:id` — Delete Stock Taking Report Items
- `GET /v1/stock-taking-report-items/:id` — Get Stock Taking Report Items
- `PATCH /v1/stock-taking-report-items/:id` — Update Stock Taking Report Items
    - body: stock_taking_report_id ((required, exists:stock_taking_reports.id)), product_id ((required, exists:products.id)), work_order_id ((optional, exists:work_orders.id)), quantity1 ((required)), quantity2 ((optional)), serials1 ((optional)), serials1_new ((optional)), serials2 ((optional)), serials2_new ((optional)), system_serials ((optional)), system_quantity ((optional)), note ((optional))
- `GET /v1/stock-taking-report-items/:id/serials` — Get Stock Taking Report Item Serials
- `GET /v1/stock-taking-report-items/all` — Get All Stock Taking Report Items

## Stock_Taking_Reports
- `GET /v1/stock-taking-reports` — Paginate Stock Taking reports
- `POST /v1/stock-taking-reports` — Create Stock Taking Reports
    - body: stock_taking_id ((required, exists:stock_takings.id)), warehouse_location_id ((required, exists:warehouse_locations.id)), order_purchase_id ((optional, exists:orders_purchase.id)), counter1_user_id ((optional, exists:users.id)), counter2_user_id ((optional, exists:users.id)), controller_user_id ((optional, exists:users.id)), date_taking ((required)), counter1_finished ((optional)), counter2_finished ((optional))
- `POST /v1/stock-taking-reports` — Create Stock Taking Reports
    - body: stock_taking_id ((required, exists:stock_takings.id)), warehouse_location_id ((required, exists:warehouse_locations.id)), order_purchase_id ((optional, exists:orders_purchase.id)), counter1_user_id ((optional, exists:users.id)), counter2_user_id ((optional, exists:users.id)), controller_user_id ((optional, exists:users.id)), date_taking ((required)), counter1_finished ((optional)), counter2_finished ((optional))
- `POST /v1/stock-taking-reports` — Create Stock Taking Reports
    - body: stock_taking_id ((required, exists:stock_takings.id)), warehouse_location_id ((required, exists:warehouse_locations.id)), order_purchase_id ((optional, exists:orders_purchase.id)), counter1_user_id ((optional, exists:users.id)), counter2_user_id ((optional, exists:users.id)), controller_user_id ((optional, exists:users.id)), date_taking ((required)), counter1_finished ((optional)), counter2_finished ((optional))
- `DELETE /v1/stock-taking-reports/:id` — Delete Stock Taking Reports
- `GET /v1/stock-taking-reports/:id` — Get Stock Taking Reports
- `PATCH /v1/stock-taking-reports/:id` — Update Stock Taking Reports
    - body: stock_taking_id ((required, exists:stock_takings.id)), warehouse_location_id ((required, exists:warehouse_locations.id)), order_purchase_id ((optional, exists:orders_purchase.id)), counter1_user_id ((optional, exists:users.id)), counter2_user_id ((optional, exists:users.id)), controller_user_id ((optional, exists:users.id)), date_taking ((required)), counter1_finished ((optional)), counter2_finished ((optional))
- `GET /v1/stock-taking-reports/all` — Get All Stock Taking Reports

## Stock_Takings
- `GET /v1/obsolete-stock` — Paginate Obsolete Stock
- `GET /v1/obsolete-stock-report/all` — Get All Obsolete Stock Reports
- `GET /v1/stock-takings` — Paginate Stock Takings
- `GET /v1/stock-takings` — Paginate Stock Takings
- `GET /v1/stock-takings` — Paginate Stock Takings
- `POST /v1/stock-takings` — Create Stock Taking
    - body: date_taking ((required)), name ((required, max:255)), member1_user_id ((optional, exists:users.id)), member2_user_id ((optional, exists:users.id)), president_user_id ((optional, exists:users.id)), counter_pairs ((required, data)), included_warehouses ((data)), excluded_warehouses ((data)), included_warehouse_locations ((data)), excluded_warehouse_locations ((data)), product_types ((data)), product_classifications ((data)), warehouse_team ((data)), ceo_full_name ((optional, max:255))
- `DELETE /v1/stock-takings/:id` — Delete Stock Taking
- `GET /v1/stock-takings/:id` — Get Stock Taking
- `PATCH /v1/stock-takings/:id` — Update Stock Takings
    - body: date_taking ((required)), name ((required, max:255)), member1_user_id ((optional, exists:users.id)), member2_user_id ((optional, exists:users.id)), president_user_id ((optional, exists:users.id)), counter_pairs ((required, data)), included_warehouses ((data)), excluded_warehouses ((data)), included_warehouse_locations ((data)), excluded_warehouse_locations ((data)), product_types ((data)), product_classifications ((data)), warehouse_team ((data)), ceo_full_name ((optional, max:255))
- `GET /v1/stock-takings/all` — Get All Stock Takings
- `GET /v1/stock-takings/all` — Get All Stock Takings

## Stock_Transactions
- `GET /v1/stock-transactions` — Paginate Stock Transactions
- `GET /v1/stock-transactions/:id` — Get Stock Transaction
- `GET /v1/stock-transactions/:id` — Get Stock Transaction
- `GET /v1/stock-transactions/all` — Get All Stock Transactions
- `GET /v1/stock-transactions/all` — Get All Stock Transactions
- `POST /v1/stock-transactions/replace-serials` — Stock Transactions Replace serials

## Stocks
- `GET /v1/stocks` — Paginate Stocks
- `POST /v1/stocks` — Create Stock
    - body: name ((required)), date ((required)), amount ((required)), description ((optional))
- `DELETE /v1/stocks/:id` — Delete Stock
- `GET /v1/stocks/:id` — Get Stocks
- `PATCH /v1/stocks/:id` — Update Stock
    - body: name ((required)), date ((required)), amount ((required)), description ((optional))
- `GET /v1/stocks/all` — Get All Stocks
- `GET /v1/stocks/dashboard` — Get dashboard stock values
- `GET /v1/stocks/personal` — Get personal stock values

## Support_Inquiries
- `GET /v1/support-inquiries` — Index Support Inquiry
- `POST /v1/support-inquiries` — Create Support Inquiry
    - body: contact_name ((optional, max:255)), contact_company ((optional, max:255)), contact_email ((optional, max:255)), contact_phone ((optional, max:255)), contact_country_id ((required, alpha, exists:countries.id)), contact_city ((optional, max:255)), contact_post ((optional, max:16)), support_type ((optional, max:255)), support_message ((optional))
- `DELETE /v1/support-inquiries/:id` — Delete Support Inquiry
- `GET /v1/support-inquiries/:id` — Get Support Inquiry
- `PATCH /v1/support-inquiries/:id` — Update Support Inquiry
    - body: contact_name ((optional, max:255)), contact_company ((optional, max:255)), contact_email ((optional, max:255)), contact_phone ((optional, max:255)), contact_country_id ((required, alpha, exists:countries.id)), contact_city ((optional, max:255)), contact_post ((optional, max:16)), support_type ((optional, max:255)), support_message ((optional))
- `GET /v1/support-inquiries/all` — Get Support Inquiry

## Sync_Bank_Account_Transactions
- `POST /v1/bank-account-transactions-sync/:applicationId` — Sync bank account transactions
    - body: partner_id ((optional, exists:partners,id)), bank_account_id ((required, bank_accounts,id)), transaction_id ((optional)), amount_inflow ((optional)), amount_outflow ((optional)), bank_commission ((optional)), currency_rate ((required)), name ((required, max:255)), date_transaction ((required)), bank_transaction_source_id ((required, exists:bank_transaction_sources.id)), amount_inflow_total ((optional)), amount_outflow_total ((optional))

## Tags
- `GET /v1/tags` — Lists All Tags
- `POST /v1/tags` — Create Tag
    - body: partner_id ((required, exists:tags.id)), name ((required, max:255)), full_path_name ((optional)), slug ((optional, unique:tags, slug)), description ((optional)), type ((optional)), table_name ((required, max:255)), order_column ((optional))
- `DELETE /v1/tags/:id` — Delete Tag
- `GET /v1/tags/:id` — Get Tag
- `PATCH /v1/tags/:id` — Update Tag
    - body: partner_id ((required, exists:tags.id)), name ((required, max:255)), full_path_name ((optional)), slug ((optional, unique:tags, slug)), description ((optional)), type ((optional)), table_name ((required, max:255)), order_column ((optional))
- `POST /v1/tags/:id/sync-data` — Sync data to related tags
- `GET /v1/tags/all` — Get all Tags
- `GET /v1/tags/get-table-types` — Get Table types
- `GET /v1/tags/price-list` — Get Tags
- `POST /v1/tags/update-sorting` — Update sorting Tags
    - body: tags ((required))

## Tariff_Codes
- `GET /v1/tariff-codes` — Paginate Tariff Codes
- `POST /v1/tariff-codes` — Create Tariff Code
- `DELETE /v1/tariff-codes/:id` — Delete Tariff Codes
- `GET /v1/tariff-codes/:id` — Get Tariff Codes
- `PATCH /v1/tariff-codes/:id` — Update Tariff Codes
    - body: name ((required, max:20)), code ((required, max:20)), description ((optional)), intrastat ((required)), enabled ((required)), intrastat_export_quantity ((required))
- `GET /v1/tariff-codes/all` — Get All Tariff Codes

## Tasks
- `GET /v1/document-tasks` — Paginate Tasks
- `POST /v1/document-tasks` — Create Task
    - body: technology_id ((required, exists:technologies.id)), document_task_id ((optional, exists:technologies.id)), name ((required)), description ((optional)), date_due ((required)), date_started ((optional, format:Y-m-d H:i:s)), date_completed ((optional, format:Y-m-d H:i:s)), resource_id ((optional, exists:resources.id)), model_id ((optional)), model_type ((optional)), vue_component ((optional))
- `DELETE /v1/document-tasks/:id` — Delete Task
- `GET /v1/document-tasks/:id` — Get Task
- `PATCH /v1/document-tasks/:id` — Update Task
    - body: technology_id ((required, exists:technologies.id)), document_task_id ((optional, exists:technologies.id)), name ((required)), description ((optional)), date_due ((required)), date_started ((optional, format:Y-m-d H:i:s)), date_completed ((optional, format:Y-m-d H:i:s)), resource_id ((optional, exists:resources.id)), model_id ((optional)), model_type ((optional)), vue_component ((optional))
- `GET /v1/document-tasks/all` — Get All Tasks
- `GET /v1/tasks` — Paginate Tasks
- `POST /v1/tasks` — Create Task
    - body: technology_id ((required, exists:technologies.id)), document_task_id ((optional, exists:technologies.id)), name ((required)), description ((optional)), date_due ((required)), date_started ((optional, format:Y-m-d H:i:s)), date_completed ((optional, format:Y-m-d H:i:s)), resource_id ((optional, exists:resources.id)), model_id ((optional)), model_type ((optional)), vue_component ((optional))
- `DELETE /v1/tasks/:id` — Delete Task
- `GET /v1/tasks/:id` — Get Task
- `PATCH /v1/tasks/:id` — Update Task
    - body: technology_id ((required, exists:technologies.id)), document_task_id ((optional, exists:technologies.id)), name ((required)), description ((optional)), date_due ((required)), date_started ((optional, format:Y-m-d H:i:s)), date_completed ((optional, format:Y-m-d H:i:s)), resource_id ((optional, exists:resources.id)), model_id ((optional)), model_type ((optional)), vue_component ((optional))
- `PATCH /v1/tasks/:id` — Update Task
    - body: technology_id ((required, exists:technologies.id)), document_task_id ((optional, exists:technologies.id)), name ((required)), description ((optional)), date_due ((required)), date_started ((optional, format:Y-m-d H:i:s)), date_completed ((optional, format:Y-m-d H:i:s)), resource_id ((optional, exists:resources.id)), model_id ((optional)), model_type ((optional)), vue_component ((optional))
- `PATCH /v1/tasks/:id` — Update Task
    - body: technology_id ((required, exists:technologies.id)), document_task_id ((optional, exists:technologies.id)), name ((required)), description ((optional)), date_due ((required)), date_started ((optional, format:Y-m-d H:i:s)), date_completed ((optional, format:Y-m-d H:i:s)), resource_id ((optional, exists:resources.id)), model_id ((optional)), model_type ((optional)), vue_component ((optional))
- `PATCH /v1/tasks/:id` — Update Task
    - body: technology_id ((required, exists:technologies.id)), document_task_id ((optional, exists:technologies.id)), name ((required)), description ((optional)), date_due ((required)), date_started ((optional, format:Y-m-d H:i:s)), date_completed ((optional, format:Y-m-d H:i:s)), resource_id ((optional, exists:resources.id)), model_id ((optional)), model_type ((optional)), vue_component ((optional))
- `PATCH /v1/tasks/:id/complete-steps` — Complete steps
    - body: technology_id ((required, exists:technologies.id)), document_task_id ((optional, exists:technologies.id)), name ((required)), description ((optional)), date_due ((required)), date_started ((optional, format:Y-m-d H:i:s)), date_completed ((optional, format:Y-m-d H:i:s)), resource_id ((optional, exists:resources.id)), model_id ((optional)), model_type ((optional)), vue_component ((optional))
- `POST /v1/tasks/:id/reopen` — Reopen Task
    - body: technology_id ((required, exists:technologies.id)), document_task_id ((optional, exists:technologies.id)), name ((required)), description ((optional)), date_due ((required)), date_started ((optional, format:Y-m-d H:i:s)), date_completed ((optional, format:Y-m-d H:i:s)), resource_id ((optional, exists:resources.id)), model_id ((optional)), model_type ((optional)), vue_component ((optional))
- `PATCH /v1/tasks/:id/start` — Start Task
    - body: technology_id ((required, exists:technologies.id)), document_task_id ((optional, exists:technologies.id)), name ((required)), description ((optional)), date_due ((required)), date_started ((optional, format:Y-m-d H:i:s)), date_completed ((optional, format:Y-m-d H:i:s)), resource_id ((optional, exists:resources.id)), model_id ((optional)), model_type ((optional)), vue_component ((optional))
- `PATCH /v1/tasks/:id/start-cnc-reservation` — Start CNC reservation Task
    - body: technology_id ((required, exists:technologies.id)), document_task_id ((optional, exists:technologies.id)), name ((required)), description ((optional)), date_due ((required)), date_started ((optional, format:Y-m-d H:i:s)), date_completed ((optional, format:Y-m-d H:i:s)), resource_id ((optional, exists:resources.id)), model_id ((optional)), model_type ((optional)), vue_component ((optional))
- `GET /v1/tasks/all` — Get All Tasks
- `GET /v1/tasks/all` — Get All Tasks
- `POST /v1/tasks/create-reservation` — Create Reservation Task
    - body: technology_id ((required, exists:technologies.id)), document_task_id ((optional, exists:technologies.id)), name ((required)), description ((optional)), date_due ((required)), date_started ((optional, format:Y-m-d H:i:s)), date_completed ((optional, format:Y-m-d H:i:s)), resource_id ((optional, exists:resources.id)), model_id ((optional)), model_type ((optional)), vue_component ((optional))
- `POST /v1/tasks/create-reservation` — Create Reservation Task
    - body: technology_id ((required, exists:technologies.id)), document_task_id ((optional, exists:technologies.id)), name ((required)), description ((optional)), date_due ((required)), date_started ((optional, format:Y-m-d H:i:s)), date_completed ((optional, format:Y-m-d H:i:s)), resource_id ((optional, exists:resources.id)), model_id ((optional)), model_type ((optional)), vue_component ((optional))
- `POST /v1/tasks/create-runner` — Create Runner Task
    - body: technology_id ((required, exists:technologies.id)), document_task_id ((optional, exists:technologies.id)), name ((required)), description ((optional)), date_due ((required)), date_started ((optional, format:Y-m-d H:i:s)), date_completed ((optional, format:Y-m-d H:i:s)), resource_id ((optional, exists:resources.id)), model_id ((optional)), model_type ((optional)), vue_component ((optional))

## Tax_Rates
- `GET /v1/tax-rates` — Paginate Tax Rates
- `POST /v1/tax-rates` — Create Tax Rate
    - body: name ((required, max:255)), code ((optional)), rate ((required)), valid_through ((optional, date_format:Y-m-d H:i:s)), description ((optional))
- `DELETE /v1/tax-rates/:id` — Delete Tax Rates
- `GET /v1/tax-rates/:id` — Get Tax Rate
- `PATCH /v1/tax-rates/:id` — Update Tax Rate
    - body: name ((required, max:255)), code ((optional)), rate ((required)), valid_through ((optional, date_format:Y-m-d H:i:s)), description ((optional))
- `GET /v1/tax-rates/all` — Get All Tax Rates

## Technologies
- `GET /v1/technologies` — Lists All Technologies
- `POST /v1/technologies` — Create Technology
    - body: assigned_user_id ((optional, exists:users.id)), assigned_resource_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), buffer_warehouse_id ((optional, exists:warehouses.id)), name ((required, max:255)), description ((optional)), technology_type ((optional, in:Start/Stop per piece, Start/Stop per work order, Event)), amount_hour_rate ((required)), vue_component ((optional)), use_in_planning ((optional)), startup_time ((optional)), fixed_time ((optional))
- `DELETE /v1/technologies/:id` — Delete Technology
- `GET /v1/technologies/:id` — Get Technology
- `PATCH /v1/technologies/:id` — Update Technology
    - body: assigned_user_id ((optional, exists:users.id)), assigned_resource_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), buffer_warehouse_id ((optional, exists:warehouses.id)), name ((required, max:255)), description ((optional)), technology_type ((optional, in:Start/Stop per piece, Start/Stop per work order, Event)), amount_hour_rate ((required)), vue_component ((optional)), use_in_planning ((optional)), startup_time ((optional)), fixed_time ((optional))
- `GET /v1/technologies/:id/backlog-history` — Get Technology backlog history
- `GET /v1/technologies/all` — Get All Technologies
- `GET /v1/technology-steps` — Lists All Technology steps
- `POST /v1/technology-steps` — Create Technology Step
    - body: vue_component ((optional)), name ((required, max:255)), description ((optional))
- `DELETE /v1/technology-steps/:id` — Delete Technology step
- `GET /v1/technology-steps/:id` — Get Technology step
- `PATCH /v1/technology-steps/:id` — Update Technology Step
    - body: vue_component ((optional)), name ((required, max:255)), description ((optional))
- `GET /v1/technology-steps/all` — Get All Technology steps

## TemplateTypes
- `GET /v1/template_types` — Paginate TemplateTypes
- `POST /v1/template_types` — Create TemplateType
    - body: name ((required)), description ((optional))
- `DELETE /v1/template_types/:id` — Delete TemplateType
- `GET /v1/template_types/:id` — Get TemplateType
- `PATCH /v1/template_types/:id` — Update TemplateType
    - body: name ((required)), description ((optional))
- `GET /v1/template_types/all` — Get All TemplateTypes

## Templates
- `GET /v1/templates` — Paginate Templates
- `POST /v1/templates` — Create Template
    - body: template_type_id ((required, exists:template_types.id)), document_type_id ((required, exists:document_types.id)), name ((required)), content ((optional)), layout ((optional)), landscape ((optional)), active ((optional))
- `DELETE /v1/templates/:id` — Delete Template
- `GET /v1/templates/:id` — Get Template
- `PATCH /v1/templates/:id` — Update Template
    - body: template_type_id ((required, exists:template_types.id)), document_type_id ((required, exists:document_types.id)), name ((required)), content ((optional)), layout ((optional)), landscape ((optional)), active ((optional))
- `GET /v1/templates/all` — Get All Templates
- `GET /v1/templates/get-format-functions` — Get format function

## Timeline
- `DELETE /v1/timeline_items` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/timeline_items` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/timeline_items` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/timeline_items` — Endpoint title here..
    - body: parameters (here..)
- `POST /v1/timeline_items` — Endpoint title here..
    - body: parameters (here..)
- `PUT /v1/timeline_items` — Endpoint title here..
    - body: parameters (here..)
- `PUT /v1/timeline_items` — Endpoint title here..
    - body: parameters (here..)
- `DELETE /v1/timeline_resource_capacities` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/timeline_resource_capacities` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/timeline_resource_capacities` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/timeline_resource_capacities` — Endpoint title here..
    - body: parameters (here..)
- `POST /v1/timeline_resource_capacities` — Endpoint title here..
    - body: parameters (here..)
- `PUT /v1/timeline_resource_capacities` — Endpoint title here..
    - body: parameters (here..)
- `DELETE /v1/timeline_resources` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/timeline_resources` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/timeline_resources` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/timeline_resources` — Endpoint title here..
    - body: parameters (here..)
- `POST /v1/timeline_resources` — Endpoint title here..
    - body: parameters (here..)
- `PUT /v1/timeline_resources` — Endpoint title here..
    - body: parameters (here..)
- `DELETE /v1/timelines` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/timelines` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/timelines` — Endpoint title here..
    - body: parameters (here..)
- `GET /v1/timelines` — Endpoint title here..
    - body: parameters (here..)
- `POST /v1/timelines` — Endpoint title here..
    - body: parameters (here..)
- `PUT /v1/timelines` — Endpoint title here..
    - body: parameters (here..)

## UndoHistory
- `GET /v1/undo-histories` — Paginate UndoHistory
- `POST /v1/undo-histories` — Create Undo History
- `DELETE /v1/undo-histories/:id` — Delete Undo History
- `GET /v1/undo-histories/:id` — Get UndoHistory
- `PATCH /v1/undo-histories/:id` — Update UndoHistory
- `GET /v1/undo-histories/all` — Get All Undo histories
- `GET /v1/undo-latest/:model/:id` — Get latest UndoHistory
- `POST /v1/undo-latest/:model/:id` — Execute latest UndoHistory

## Units
- `GET /v1/units` — Paginate Units
- `POST /v1/units` — Create Unit
    - body: name ((required, max:255))
- `DELETE /v1/units/:id` — Delete Unit
- `GET /v1/units/:id` — Get Unit
- `PATCH /v1/units/:id` — Update Unit
    - body: name ((required, max:255))
- `GET /v1/units/all` — Get All Units

## Upgrades
- `GET /v1/upgrades` — Paginate Upgrades
- `POST /v1/upgrades` — Create Upgrade
    - body: order_sale_item_id ((optional, exists:order_sale_items.id)), serial_id ((optional, exists:serials.id)), handling_country_id ((required, exists:countries.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional, max:255)), external_reference_number ((optional, max:255)), upgrade_report_number ((optional, max:32)), customer_upgrade_description ((optional)), request_firmware_update ((optional)), upgrade_team_coordinator_user_id ((optional, exists:users.id)), upgrade_package_description ((optional)), upgrade_implemented_actions ((optional)), firmware_update ((optional)), calibration ((optional)), upgrade_type_upgrade ((optional)), upgrade_type_recalibration ((optional)), upgrade_type_none ((optional)), upgrade_team_recognition ((optional)), upgrade_note ((optional)), upgrade_time ((optional)), date_received ((optional, format:Y-m-d H:i:s)), date_shipped ((optional, format:Y-m-d H:i:s)), date_closed ((optional, format:Y-m-d H:i:s)), date_estimated_amount_confirmed ((optional, format:Y-m-d H:i:s)), estimated_amount_confirmed ((optional)), currency_code_id ((optional, alpha, exists:currency_codes.id)), amount_estimated_currency ((required)), upgrade_box_number ((optional))
- `DELETE /v1/upgrades/:id` — Delete Upgrade Upgrades
- `GET /v1/upgrades/:id` — Get Upgrades
- `PATCH /v1/upgrades/:id` — Update Upgrades
    - body: order_sale_item_id ((optional, exists:order_sale_items.id)), serial_id ((optional, exists:serials.id)), handling_country_id ((required, exists:countries.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional, max:255)), external_reference_number ((optional, max:255)), upgrade_report_number ((optional, max:32)), customer_upgrade_description ((optional)), request_firmware_update ((optional)), upgrade_team_coordinator_user_id ((optional, exists:users.id)), upgrade_package_description ((optional)), upgrade_implemented_actions ((optional)), firmware_update ((optional)), calibration ((optional)), upgrade_type_upgrade ((optional)), upgrade_type_recalibration ((optional)), upgrade_type_none ((optional)), upgrade_team_recognition ((optional)), upgrade_note ((optional)), upgrade_time ((optional)), date_received ((optional, format:Y-m-d H:i:s)), date_shipped ((optional, format:Y-m-d H:i:s)), date_closed ((optional, format:Y-m-d H:i:s)), date_estimated_amount_confirmed ((optional, format:Y-m-d H:i:s)), estimated_amount_confirmed ((optional)), currency_code_id ((optional, alpha, exists:currency_codes.id)), amount_estimated_currency ((required)), upgrade_box_number ((optional))
- `PATCH /v1/upgrades/:id` — Update Upgrades
    - body: order_sale_item_id ((optional, exists:order_sale_items.id)), serial_id ((optional, exists:serials.id)), handling_country_id ((required, exists:countries.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional, max:255)), external_reference_number ((optional, max:255)), upgrade_report_number ((optional, max:32)), customer_upgrade_description ((optional)), request_firmware_update ((optional)), upgrade_team_coordinator_user_id ((optional, exists:users.id)), upgrade_package_description ((optional)), upgrade_implemented_actions ((optional)), firmware_update ((optional)), calibration ((optional)), upgrade_type_upgrade ((optional)), upgrade_type_recalibration ((optional)), upgrade_type_none ((optional)), upgrade_team_recognition ((optional)), upgrade_note ((optional)), upgrade_time ((optional)), date_received ((optional, format:Y-m-d H:i:s)), date_shipped ((optional, format:Y-m-d H:i:s)), date_closed ((optional, format:Y-m-d H:i:s)), date_estimated_amount_confirmed ((optional, format:Y-m-d H:i:s)), estimated_amount_confirmed ((optional)), currency_code_id ((optional, alpha, exists:currency_codes.id)), amount_estimated_currency ((required)), upgrade_box_number ((optional))
- `GET /v1/upgrades/all` — Get All Upgrade Upgrades

## User_Filters
- `GET /v1/user-filters` — Paginate User Filters
- `POST /v1/user-filters` — Create User Filter
- `DELETE /v1/user-filters/:id` — Delete User Filters
- `GET /v1/user-filters/:id` — Get User Filter
- `PATCH /v1/user-filters/:id` — Update User Filter
    - body: table_name ((required)), name ((required)), user_id ((required, exists:users.id))

## User_Hr_Profile_Work_Equipment
- `DELETE /v1/user-hr-profile-work-equipment/:id` — Delete User Hr Profile Work Equipment

## User_Hr_Profile_Work_Position
- `DELETE /v1/user-hr-profile-work-position/:id` — Delete User Hr Profile Work Position

## User_Hr_Profiles
- `DELETE /v1/user-hr-profiles/:id` — Delete User Hr Profiles

## User_Work_Position
- `DELETE /v1/user-work-positions/:id` — Delete User Work Position

## User_hr_profile
- `GET /v1/user-hr-profiles` — Lists All User hr profiles
- `POST /v1/user-hr-profiles` — Create user hr profiles
    - body: emso ((required)), private_email ((required)), private_phone ((required)), gender ((required)), entry_registration ((required)), overtime ((required)), work_day_obligation ((required)), leave_days_basis ((required)), leave_days_bonus ((required)), leave_days_transfer ((required)), allow_work_from_home ((optional)), student_hourly_rate ((optional)), student_referral_number ((optional)), tax_number ((optional)), allow_shift_work ((optional)), birth_location ((optional)), date_birthday ((optional)), contracts_confirm_date ((optional)), cost_center_plain ((optional)), employment_start_date ((optional)), allow_night_work ((optional)), transportation_distance ((required)), user_id ((required, exists:users.id)), country_id ((required, exists:countries.id)), birokrat_id ((required))
- `PATCH /v1/user-hr-profiles/:id` — Update User hr profiles
    - body: emso ((required)), private_email ((required)), private_phone ((required)), gender ((required)), entry_registration ((required)), overtime ((required)), work_day_obligation ((required)), leave_days_basis ((required)), leave_days_bonus ((required)), leave_days_transfer ((required)), allow_work_from_home ((optional)), student_hourly_rate ((optional)), student_referral_number ((optional)), tax_number ((optional)), allow_shift_work ((optional)), birth_location ((optional)), date_birthday ((optional)), contracts_confirm_date ((optional)), cost_center_plain ((optional)), employment_start_date ((optional)), allow_night_work ((optional)), transportation_distance ((required)), user_id ((required, exists:users.id)), country_id ((required, exists:countries.id)), birokrat_id ((required))

## User_hr_profile_work_equipment
- `GET /v1/user-hr-profile-work-equipment` — Lists All User hr profile work equipment
- `POST /v1/user-hr-profile-work-equipment` — Create user hr profile work equipment
    - body: user_hr_profile_id ((required)), work_equipment_id ((required))
- `GET /v1/user-hr-profile-work-equipment/:id` — Get User hr profile work equipment
- `PATCH /v1/user-hr-profile-work-equipment/:id` — Update User hr profile work equipment
    - body: user_hr_profile_id ((required)), work_equipment_id ((required))
- `GET /v1/user-hr-profile-work-equipment/all` — Get all user hr-profile-work equipment

## User_hr_profile_work_position
- `GET /v1/user-hr-profile-work-position` — Lists All User hr profile work positions
- `PATCH /v1/user-hr-profile-work-position/:id` — Update User hr profile work positions
    - body: from ((required)), to ((required)), user_hr_profile_id ((required, exists:user_hr_profiles.id)), user_work_position_id ((required, exists:user_work_positions.id)), employment_type_id ((optional, exists:employment_types.id))

## User_hr_profile_work_positions
- `POST /v1/user-hr-profile-work-position` — Create user hr profile work positions
    - body: from ((required)), to ((required)), user_hr_profile_id ((required, exists:user_hr_profiles.id)), user_work_position_id ((required, exists:user_work_positions.id)), employment_type_id ((optional, exists:employment_types.id))
- `GET /v1/user-hr-profile-work-position/:id` — Get User hr profile work positions
- `GET /v1/user-hr-profile-work-position/all` — Get all user hr-profile-work positions
- `GET /v1/user-hr-profile-work-position/get-missing-promo Get all user hr-profile-work missing` — promo
- `POST /v1/user-hr-profile-work-position/start-to-distribute-products` — Start to distribute
    - body: selected_missing_stock ((required))

## User_hr_profiles
- `GET /v1/user-hr-profiles/:id` — Get User hr profiles
- `GET /v1/user-hr-profiles/all` — Get all user hr-profiles

## User_saldo_month
- `GET /v1/user-saldo-months` — Lists All User saldo months
- `POST /v1/user-saldo-months` — Create user saldo month
    - body: month ((required)), user_id ((required))
- `GET /v1/user-saldo-months/:id` — Get User saldo month
- `PATCH /v1/user-saldo-months/:id` — Update User saldo months
    - body: month ((required)), user_id ((required))

## User_work_position
- `GET /v1/hr-departments` — Lists All User work positions
- `PATCH /v1/user-work-positions/:id` — Update User work positions
    - body: name ((required)), leave_bonus ((required)), is_parent ((required)), hr_department_id ((required, exists:user_work_positions.id))

## User_work_positions
- `POST /v1/user-work-positions` — Create user work positions
    - body: name ((required)), leave_bonus ((required)), is_parent ((required)), hr_department_id ((required, exists:user_work_positions.id))
- `GET /v1/user-work-positions/:id` — Get User work positions
- `GET /v1/user-work-positions/all` — Get all user work positions

## Users
- `GET /v1/users` — Paginate Users
- `GET /v1/users` — Paginate Users
- `GET /v1/users` — Paginate Users
- `POST /v1/users` — Confirm a new User
    - body: user_vendor_id ((optional, unique:users, user_vendor_id, nullable)), parent_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), name ((optional)), username ((optional, unique:users, username)), email ((required, unique:users, email)), password ((required, confirmed, min:4)), remember_token ((required if password)), confirmed ((optional)), last_login ((optional, format:Y-m-d H:i:s)), love_reacter_id ((optional)), authentication_token ((optional, max:500)), crm_token ((optional, max:255)), confirmation_token ((optional, max:255)), account_upload_token ((optional)), card_number ((optional))
- `POST /v1/users` — Confirm a new User
    - body: user_vendor_id ((optional, unique:users, user_vendor_id, nullable)), parent_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), name ((optional)), username ((optional, unique:users, username)), email ((required, unique:users, email)), password ((required, confirmed, min:4)), remember_token ((required if password)), confirmed ((optional)), last_login ((optional, format:Y-m-d H:i:s)), love_reacter_id ((optional)), authentication_token ((optional, max:500)), crm_token ((optional, max:255)), confirmation_token ((optional, max:255)), account_upload_token ((optional)), card_number ((optional))
- `POST /v1/users` — Create User
    - body: user_vendor_id ((optional, unique:users, user_vendor_id, nullable)), parent_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), name ((optional)), username ((optional, unique:users, username)), email ((required, unique:users, email)), password ((required, confirmed, min:4)), remember_token ((required if password)), confirmed ((optional)), last_login ((optional, format:Y-m-d H:i:s)), love_reacter_id ((optional)), authentication_token ((optional, max:500)), crm_token ((optional, max:255)), confirmation_token ((optional, max:255)), account_upload_token ((optional)), card_number ((optional))
- `POST /v1/users` — Create User
    - body: user_vendor_id ((optional, unique:users, user_vendor_id, nullable)), parent_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), name ((optional)), username ((optional, unique:users, username)), email ((required, unique:users, email)), password ((required, confirmed, min:4)), remember_token ((required if password)), confirmed ((optional)), last_login ((optional, format:Y-m-d H:i:s)), love_reacter_id ((optional)), authentication_token ((optional, max:500)), crm_token ((optional, max:255)), confirmation_token ((optional, max:255)), account_upload_token ((optional)), card_number ((optional))
- `POST /v1/users` — Create User
    - body: user_vendor_id ((optional, unique:users, user_vendor_id, nullable)), parent_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), name ((optional)), username ((optional, unique:users, username)), email ((required, unique:users, email)), password ((required, confirmed, min:4)), remember_token ((required if password)), confirmed ((optional)), last_login ((optional, format:Y-m-d H:i:s)), love_reacter_id ((optional)), authentication_token ((optional, max:500)), crm_token ((optional, max:255)), confirmation_token ((optional, max:255)), account_upload_token ((optional)), card_number ((optional))
- `POST /v1/users` — Register User
    - body: user_vendor_id ((optional, unique:users, user_vendor_id, nullable)), parent_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), name ((optional)), username ((optional, unique:users, username)), email ((required, unique:users, email)), password ((required, confirmed, min:4)), remember_token ((required if password)), confirmed ((optional)), last_login ((optional, format:Y-m-d H:i:s)), love_reacter_id ((optional)), authentication_token ((optional, max:500)), crm_token ((optional, max:255)), confirmation_token ((optional, max:255)), account_upload_token ((optional)), card_number ((optional))
- `DELETE /v1/users/:id` — Delete User (admin, client..)
- `DELETE /v1/users/:id` — Delete User (admin, client..)
- `GET /v1/users/:id` — Get User
- `GET /v1/users/:id` — Get User
- `GET /v1/users/:id` — Get User
- `PATCH /v1/users/:id` — Update User
    - body: user_vendor_id ((optional, unique:users, user_vendor_id, nullable)), parent_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), name ((optional)), username ((optional, unique:users, username)), email ((required, unique:users, email)), password ((required, confirmed, min:4)), remember_token ((required if password)), confirmed ((optional)), last_login ((optional, format:Y-m-d H:i:s)), love_reacter_id ((optional)), authentication_token ((optional, max:500)), crm_token ((optional, max:255)), confirmation_token ((optional, max:255)), account_upload_token ((optional)), card_number ((optional))
- `PATCH /v1/users/:id` — Update User
    - body: user_vendor_id ((optional, unique:users, user_vendor_id, nullable)), parent_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), name ((optional)), username ((optional, unique:users, username)), email ((required, unique:users, email)), password ((required, confirmed, min:4)), remember_token ((required if password)), confirmed ((optional)), last_login ((optional, format:Y-m-d H:i:s)), love_reacter_id ((optional)), authentication_token ((optional, max:500)), crm_token ((optional, max:255)), confirmation_token ((optional, max:255)), account_upload_token ((optional)), card_number ((optional))
- `PATCH /v1/users/:id` — Update User
    - body: user_vendor_id ((optional, unique:users, user_vendor_id, nullable)), parent_id ((optional, exists:users.id)), partner_id ((optional, exists:partners.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), name ((optional)), username ((optional, unique:users, username)), email ((required, unique:users, email)), password ((required, confirmed, min:4)), remember_token ((required if password)), confirmed ((optional)), last_login ((optional, format:Y-m-d H:i:s)), love_reacter_id ((optional)), authentication_token ((optional, max:500)), crm_token ((optional, max:255)), confirmation_token ((optional, max:255)), account_upload_token ((optional)), card_number ((optional))
- `GET /v1/users/me` — Get Me
- `PATCH /v1/users/me/update` — Update self
- `GET /v1/users/self` — Get user's account data
- `GET /v1/users/self` — Get user's account data

## Warehouse_Locations
- `GET /v1/warehouse-locations` — Lists All Warehouse Locations
- `POST /v1/warehouse-locations` — Create Warehouse Location
    - body: warehouse_id ((required, exists:warehouses.id)), name ((required, max:255)), description ((optional)), default_product_line_id ((optinal, exists:product_lines.id))
- `DELETE /v1/warehouse-locations/:id` — Delete Warehouse Location
- `GET /v1/warehouse-locations/:id` — Get Warehouse Locations
- `PATCH /v1/warehouse-locations/:id` — Update Warehouse Locations
    - body: warehouse_id ((required, exists:warehouses.id)), name ((required, max:255)), description ((optional)), default_product_line_id ((optinal, exists:product_lines.id))
- `GET /v1/warehouse-locations/:id/stock-by-product` — Get Stock in Warehouse Locations by Product
- `GET /v1/warehouse-locations/:id/stock-by-product` — Get Stock in Warehouse Locations by Product
- `GET /v1/warehouse-locations/:id/stock-by-product-type Get Stock in Warehouse Locations by` — Product Type
- `GET /v1/warehouse-locations/:id/stock-transactions` — Get Warehouse Location stock transactions
- `GET /v1/warehouse-locations/all` — Get All Warehouse Locations
- `GET /v1/warehouse-locations/reservation` — Get Reservation Warehouse Location
- `GET /v1/warehouse-locations/transfers-between-work-orders Get Warehouse Location for` — transfers between work orders

## Warehouses
- `GET /v1/warehouse-locations/:id/stock-by-product-type Get Stock in Warehouse by` — Product Type
- `GET /v1/warehouse-locations/:id/stock-transactions` — Get Warehouse stock transactions
- `GET /v1/warehouses` — Paginate Warehouses
- `POST /v1/warehouses` — Create Warehouse
    - body: name ((required, max:255)), description ((optional)), production_supply ((optional)), production ((optional)), waste ((optional)), transit ((optional)), receive_goods ((optional)), promo_supply ((optional)), requirements_supply ((optional)), order_requirements_supply ((optional)), planner_supply ((optional)), is_wall ((optional))
- `DELETE /v1/warehouses/:id` — Delete Warehouse
- `GET /v1/warehouses/:id` — Get Warehouses
- `PATCH /v1/warehouses/:id` — Update Warehouse
    - body: name ((required, max:255)), description ((optional)), production_supply ((optional)), production ((optional)), waste ((optional)), transit ((optional)), receive_goods ((optional)), promo_supply ((optional)), requirements_supply ((optional)), order_requirements_supply ((optional)), planner_supply ((optional)), is_wall ((optional))
- `GET /v1/warehouses/:id/stock-by-product` — Get Stock in Warehouse by Product
- `GET /v1/warehouses/:id/stock-by-product` — Get Stock in Warehouse by Product
- `GET /v1/warehouses/all` — Get All Warehouses

## WorkOrderItem_BOMs
- `POST /v1/work-order-item-bom/:id/virtual-reservation` — Virtual reserve work order bom material
    - body: quantity ((optional))

## Work_Equipment
- `POST /v1/work-equipment` — Create work equipment
    - body: name ((required))
- `DELETE /v1/work-equipment/:id` — Delete Work Equipment
- `GET /v1/work-equipment/:id` — Get Work Equipment
- `PATCH /v1/work-equipment/:id` — Update Work Equipment
    - body: name ((required))
- `GET /v1/work-equipment/all` — Get all work equipment

## Work_Location
- `DELETE /v1/work-locations/:id` — Delete Work Location

## Work_Locations
- `GET /v1/work-locations/all` — Get all work locations

## Work_Order_BOMs
- `GET /v1/bom-technology-steps` — Paginate Work order Technology steps
- `POST /v1/bom-technology-steps` — Create Work order item technology step
    - body: bom_technology_id ((required, exists:bom_technology.id)), technology_step_id ((required, exists:technology_steps.id)), start_with ((optional)), repeat_every ((optional)), question ((optional)), measure ((optional)), offset_min ((optional)), offset_max ((optional)), unit_id ((optional)), sort_order ((optional)), general ((optional)), group ((optional))
- `DELETE /v1/bom-technology-steps/:id` — Delete Work order item technology step
- `GET /v1/bom-technology-steps/:id` — Get Work order item technology step
- `PATCH /v1/bom-technology-steps/:id` — Update Work order Technology Step
    - body: bom_technology_id ((required, exists:bom_technology.id)), technology_step_id ((required, exists:technology_steps.id)), start_with ((optional)), repeat_every ((optional)), question ((optional)), measure ((optional)), offset_min ((optional)), offset_max ((optional)), unit_id ((optional)), sort_order ((optional)), general ((optional)), group ((optional))
- `GET /v1/bom-technology-steps/all` — Get All Work order item technology steps
- `GET /v1/work-order-item-bom` — Paginate Work order BOM
- `POST /v1/work-order-item-bom` — Create Work order BOM
    - body: work_order_item_id ((required, exists:work_order_items.id)), product_id ((required, exists:products.id)), quantity ((required)), quantity_total ((optional)), quantity_used ((optional)), quantity_virtual_reservation ((optional)), quantity_physical_reservation ((optional)), date_available (Date)
- `GET /v1/work-order-item-bom-picker-sorted/all` — Get All Work order BOMs
- `DELETE /v1/work-order-item-bom/:id` — Delete Work order BOM
- `GET /v1/work-order-item-bom/:id` — Get Work order BOM
- `PATCH /v1/work-order-item-bom/:id` — Update Work order BOM
    - body: work_order_item_id ((required, exists:work_order_items.id)), product_id ((required, exists:products.id)), quantity ((required)), quantity_total ((optional)), quantity_used ((optional)), quantity_virtual_reservation ((optional)), quantity_physical_reservation ((optional)), date_available (Date)
- `GET /v1/work-order-item-bom/all` — Get All Work order BOMs
- `GET /v1/work-order-item-steps` — Paginate Work order steps
- `POST /v1/work-order-item-steps` — Create Work order item step
    - body: work_order_item_technology_id ((required, exists:work_order_item_technology_steps.id)), assigned_user_id ((optional, exists:users.id)), started_at ((optional)), serial_id ((optional, exists:serials.id)), sort_order ((optional)), total_time ((optional)), measure ((optional)), date_completed ((optional))
- `DELETE /v1/work-order-item-steps/:id` — Delete Work order item step
- `GET /v1/work-order-item-steps/:id` — Get Work order item step
- `PATCH /v1/work-order-item-steps/:id` — Update Work order Step
    - body: work_order_item_technology_id ((required, exists:work_order_item_technology_steps.id)), assigned_user_id ((optional, exists:users.id)), started_at ((optional)), serial_id ((optional, exists:serials.id)), sort_order ((optional)), total_time ((optional)), measure ((optional)), date_completed ((optional))
- `POST /v1/work-order-item-steps/:id/complete` — Complete Work order item step
- `POST /v1/work-order-item-steps/:id/pause` — Pause Work order item step
- `POST /v1/work-order-item-steps/:id/start` — Start Work order item step
- `GET /v1/work-order-item-steps/all` — Get All Work order item steps
- `GET /v1/work-order-item-technologies` — Paginate Work order BOM
- `POST /v1/work-order-item-technologies` — Create Work order BOM
    - body: assigned_user_id ((optional, exists:users.id)), assigned_resource_id ((optional, exists:resources.id)), assigned_resource_rank ((optional)), sort_order ((optional)), work_order_item_id ((required, exists:work_order_items.id)), work_order_item_technology_dependency_id ((optional, exists:work_order_item_technology.id)), technology_id ((required, exists:technologies.id)), amount ((optional, min:0)), amount_per_hour ((optional)), task_id ((optional, exists:tasks.id)), date_start ((optional)), date_start_earliest ((optional)), date_capacity_available_at ((optional)), date_start_user ((optional)), date_stop ((optional)), use_in_planning ((optional)), planning_locked_at ((optional)), manually_assigned_resource_id ((optional, exists:resources.id)), duration ((optional)), capacity_wait_time ((optional, EXTRACT(epoch from {table_name}.date_start - {table_name}.date_start_earliest))), dependency_wait_time ((optional, EXTRACT(epoch from {table_name}.date_start - {table_name}.date_capacity_available_at))), startup_time ((optional))
- `POST /v1/work-order-item-technologies` — Create Work order BOM
    - body: assigned_user_id ((optional, exists:users.id)), assigned_resource_id ((optional, exists:resources.id)), assigned_resource_rank ((optional)), sort_order ((optional)), work_order_item_id ((required, exists:work_order_items.id)), work_order_item_technology_dependency_id ((optional, exists:work_order_item_technology.id)), technology_id ((required, exists:technologies.id)), amount ((optional, min:0)), amount_per_hour ((optional)), task_id ((optional, exists:tasks.id)), date_start ((optional)), date_start_earliest ((optional)), date_capacity_available_at ((optional)), date_start_user ((optional)), date_stop ((optional)), use_in_planning ((optional)), planning_locked_at ((optional)), manually_assigned_resource_id ((optional, exists:resources.id)), duration ((optional)), capacity_wait_time ((optional, EXTRACT(epoch from {table_name}.date_start - {table_name}.date_start_earliest))), dependency_wait_time ((optional, EXTRACT(epoch from {table_name}.date_start - {table_name}.date_capacity_available_at))), startup_time ((optional))
- `DELETE /v1/work-order-item-technologies/:id` — Delete Work order BOM
- `GET /v1/work-order-item-technologies/:id` — Get Work order BOM
- `PATCH /v1/work-order-item-technologies/:id` — Update Work order BOM
    - body: assigned_user_id ((optional, exists:users.id)), assigned_resource_id ((optional, exists:resources.id)), assigned_resource_rank ((optional)), sort_order ((optional)), work_order_item_id ((required, exists:work_order_items.id)), work_order_item_technology_dependency_id ((optional, exists:work_order_item_technology.id)), technology_id ((required, exists:technologies.id)), amount ((optional, min:0)), amount_per_hour ((optional)), task_id ((optional, exists:tasks.id)), date_start ((optional)), date_start_earliest ((optional)), date_capacity_available_at ((optional)), date_start_user ((optional)), date_stop ((optional)), use_in_planning ((optional)), planning_locked_at ((optional)), manually_assigned_resource_id ((optional, exists:resources.id)), duration ((optional)), capacity_wait_time ((optional, EXTRACT(epoch from {table_name}.date_start - {table_name}.date_start_earliest))), dependency_wait_time ((optional, EXTRACT(epoch from {table_name}.date_start - {table_name}.date_capacity_available_at))), startup_time ((optional))
- `GET /v1/work-order-item-technologies/:id/task` — Create work order item technology task
- `GET /v1/work-order-item-technologies/:id/task` — Generate work order item steps
- `GET /v1/work-order-item-technologies/all` — Get All Work order BOMs
- `GET /v1/work-order-item-technology-steps` — Paginate Work order Technology steps
- `POST /v1/work-order-item-technology-steps` — Create Work order item technology step
    - body: work_order_item_technology_id ((required, exists:work_order_item_technology.id)), technology_step_id ((required, exists:technology_steps.id)), start_with ((optional)), repeat_every ((optional)), question ((optional)), measure ((optional)), offset_min ((optional)), offset_max ((optional)), unit_id ((optional, exists:units.id)), sort_order ((optional)), general ((optional)), group ((optional))
- `DELETE /v1/work-order-item-technology-steps/:id` — Delete Work order item technology step
- `GET /v1/work-order-item-technology-steps/:id` — Get Work order item technology step
- `PATCH /v1/work-order-item-technology-steps/:id` — Update Work order Technology Step
    - body: work_order_item_technology_id ((required, exists:work_order_item_technology.id)), technology_step_id ((required, exists:technology_steps.id)), start_with ((optional)), repeat_every ((optional)), question ((optional)), measure ((optional)), offset_min ((optional)), offset_max ((optional)), unit_id ((optional, exists:units.id)), sort_order ((optional)), general ((optional)), group ((optional))
- `GET /v1/work-order-item-technology-steps/all` — Get All Work order item technology steps

## Work_Order_Items
- `GET /v1/new-picker-work-order-items/` — Get Work Order items for picker view

## Work_Orders
- `POST /v1/work-order-item/{work_order_item_id}/bom` — Create Work order BOM
    - body: work_order_item_id ((required, exists:work_order_items.id)), product_id ((required, exists:products.id)), quantity ((required)), quantity_total ((optional)), quantity_used ((optional)), quantity_virtual_reservation ((optional)), quantity_physical_reservation ((optional)), date_available (Date)
- `GET /v1/work-order-items` — Paginate Work Order items
- `POST /v1/work-order-items` — Create Payment Method
    - body: work_order_id ((required, exists:work_orders.id)), parent_work_order_item_id ((optional, exists:work_order_items.id)), product_id ((optional, exists:products.id)), bom_id ((optional, exists:bom.id)), order_sale_item_id ((optional, exists:order_sale_items.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), quantity ((required)), quantity_receipt ((required)), date_due ((optional, format:Y-m-d H:i:s)), date_material_due ((optional, format:Y-m-d H:i:s)), date_stop_expected ((optional)), date_start_expected ((optional)), use_in_planning ((optional)), planning_priority ((optional)), planning_ordinal ((optional)), planning_parent_id ((optional)), date_delivery_expected ((optional))
- `DELETE /v1/work-order-items/:id` — Delete Word Order
- `GET /v1/work-order-items/:id` — Get Work Order item
- `PATCH /v1/work-order-items/:id` — Update Work Order item
    - body: work_order_id ((required, exists:work_orders.id)), parent_work_order_item_id ((optional, exists:work_order_items.id)), product_id ((optional, exists:products.id)), bom_id ((optional, exists:bom.id)), order_sale_item_id ((optional, exists:order_sale_items.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), quantity ((required)), quantity_receipt ((required)), date_due ((optional, format:Y-m-d H:i:s)), date_material_due ((optional, format:Y-m-d H:i:s)), date_stop_expected ((optional)), date_start_expected ((optional)), use_in_planning ((optional)), planning_priority ((optional)), planning_ordinal ((optional)), planning_parent_id ((optional)), date_delivery_expected ((optional))
- `PATCH /v1/work-order-items/:id` — Update Work Order item
    - body: work_order_id ((required, exists:work_orders.id)), parent_work_order_item_id ((optional, exists:work_order_items.id)), product_id ((optional, exists:products.id)), bom_id ((optional, exists:bom.id)), order_sale_item_id ((optional, exists:order_sale_items.id)), warehouse_location_id ((optional, exists:warehouse_locations.id)), quantity ((required)), quantity_receipt ((required)), date_due ((optional, format:Y-m-d H:i:s)), date_material_due ((optional, format:Y-m-d H:i:s)), date_stop_expected ((optional)), date_start_expected ((optional)), use_in_planning ((optional)), planning_priority ((optional)), planning_ordinal ((optional)), planning_parent_id ((optional)), date_delivery_expected ((optional))
- `POST /v1/work-order-items/:id` — Reset Word Order item
- `POST /v1/work-order-items/:id/add-bom-items` — Add bom items
- `POST /v1/work-order-items/:id/add-bom-to-bom` — Add bom from product
- `POST /v1/work-order-items/:id/add-serials` — Add serials
- `POST /v1/work-order-items/:id/add-to-bom` — Add to work order item bom
    - body: serials ((required if work order has serials)), quantity ((required)), product_id ((required)), add ((optional))
- `GET /v1/work-order-items/:id/bom` — Get Work Order item sum bom
- `GET /v1/work-order-items/:id/cooperations` — Get Work Order item cooperations
- `GET /v1/work-order-items/:id/cooperations` — Get Work Order item cooperations
- `GET /v1/work-order-items/:id/material` — Get Work Order item material
- `GET /v1/work-order-items/:id/material` — Get Work Order item material
- `POST /v1/work-order-items/:id/material-flow` — Material flow for work order
- `POST /v1/work-order-items/:id/move-material` — Move material
- `POST /v1/work-order-items/:id/move-material-to-warehouse-location Move material to warehouse` — location
- `POST /v1/work-order-items/:id/pending-transfer/:userId Create pending transfer for work order` — item
- `POST /v1/work-order-items/:id/physical-reservation` — Physical reserve work order material
    - body: products ((required))
- `POST /v1/work-order-items/:id/physical-unreservation` — Physical unreserve work order material
    - body: products ((required))
- `POST /v1/work-order-items/:id/physical-unreservation-new` — Physical unreserve work order material
    - body: products ((required))
- `POST /v1/work-order-items/:id/receipt-fifo/` — Work order Receipt
    - body: quantity ((required)), warehouse_location_id ((optional))
- `POST /v1/work-order-items/:id/receipt/` — Work order Receipt
    - body: serials ((required if no quantity)), quantity ((required if no serials)), warehouse_location_id ((optional))
- `POST /v1/work-order-items/:id/receipt/` — Work order Receipt
    - body: serials ((required if no quantity)), quantity ((required if no serials)), warehouse_location_id ((optional))
- `POST /v1/work-order-items/:id/receipt/` — Work order Receipt
- `POST /v1/work-order-items/:id/receipt/` — Work order Receipt
- `POST /v1/work-order-items/:id/reserved-material/` — Work order Receipt
- `POST /v1/work-order-items/:id/set-fifo-material-as-used/` — Work order Receipt
- `POST /v1/work-order-items/:id/set-material-as-used/` — Work order Receipt
- `GET /v1/work-order-items/:id/stock-transactions` — Get Work Order item stock transactions
- `GET /v1/work-order-items/:id/technologieset` — Work Order item sum technologies
- `POST /v1/work-order-items/:id/transfer/:userId?` — Transfer work order material
- `POST /v1/work-order-items/:id/transfer/:userId?` — Transfer work order material
- `POST /v1/work-order-items/:id/transfer/:userId?` — Transfer work order material
- `POST /v1/work-order-items/:id/transfer/:userId?` — Transfer work order item material
- `GET /v1/work-order-items/:id/virtual-reservation` — Get virtual reserved work order material
- `POST /v1/work-order-items/:id/virtual-reservation` — Virtual reserve work order material
- `POST /v1/work-order-items/:id/virtual-reservation` — Virtual reserve work order material
- `GET /v1/work-order-items/all` — Get All Work Order items
- `GET /v1/work-order-items/get-next-technology-for-runner` — Get next technology for cart
- `GET /v1/work-order-items/get-work-order-items-for-technology/:technologyId Get Work Order` — items for cart
- `POST /v1/work-order/{work_order_id}/bom` — Create Work order BOM
    - body: work_order_item_id ((required, exists:work_order_items.id)), product_id ((required, exists:products.id)), quantity ((required)), quantity_total ((optional)), quantity_used ((optional)), quantity_virtual_reservation ((optional)), quantity_physical_reservation ((optional)), date_available (Date)
- `GET /v1/work-orders` — Paginate Work Orders
- `POST /v1/work-orders` — Create Payment Method
    - body: parent_work_order_id ((optional, exists:work_orders.id)), service_external_id ((optional, exists:services_external.id)), service_internal_id ((optional, exists:services_internal.id)), upgrade_id ((optional, exists:upgrades.id)), facility_id ((optional, exists:facilities.id)), delivery_note_issued_id ((optional, exists:delivery_notes_issued.id)), order_sale_id ((optional, exists:orders_sale.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional)), date_delivery_expected ((optional)), date_delivery_expected_first ((optional)), date_start_expected ((optional)), date_stop_expected ((optional)), date_diff ((optional)), amount_total ((optional)), priority_order ((optional)), production_planner_bin_id ((optional))
- `POST /v1/work-orders` — Create Payment Method
    - body: parent_work_order_id ((optional, exists:work_orders.id)), service_external_id ((optional, exists:services_external.id)), service_internal_id ((optional, exists:services_internal.id)), upgrade_id ((optional, exists:upgrades.id)), facility_id ((optional, exists:facilities.id)), delivery_note_issued_id ((optional, exists:delivery_notes_issued.id)), order_sale_id ((optional, exists:orders_sale.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional)), date_delivery_expected ((optional)), date_delivery_expected_first ((optional)), date_start_expected ((optional)), date_stop_expected ((optional)), date_diff ((optional)), amount_total ((optional)), priority_order ((optional)), production_planner_bin_id ((optional))
- `POST /v1/work-orders` — Create Payment Method
    - body: parent_work_order_id ((optional, exists:work_orders.id)), service_external_id ((optional, exists:services_external.id)), service_internal_id ((optional, exists:services_internal.id)), upgrade_id ((optional, exists:upgrades.id)), facility_id ((optional, exists:facilities.id)), delivery_note_issued_id ((optional, exists:delivery_notes_issued.id)), order_sale_id ((optional, exists:orders_sale.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional)), date_delivery_expected ((optional)), date_delivery_expected_first ((optional)), date_start_expected ((optional)), date_stop_expected ((optional)), date_diff ((optional)), amount_total ((optional)), priority_order ((optional)), production_planner_bin_id ((optional))
- `POST /v1/work-orders` — Create Payment Method
    - body: parent_work_order_id ((optional, exists:work_orders.id)), service_external_id ((optional, exists:services_external.id)), service_internal_id ((optional, exists:services_internal.id)), upgrade_id ((optional, exists:upgrades.id)), facility_id ((optional, exists:facilities.id)), delivery_note_issued_id ((optional, exists:delivery_notes_issued.id)), order_sale_id ((optional, exists:orders_sale.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional)), date_delivery_expected ((optional)), date_delivery_expected_first ((optional)), date_start_expected ((optional)), date_stop_expected ((optional)), date_diff ((optional)), amount_total ((optional)), priority_order ((optional)), production_planner_bin_id ((optional))
- `DELETE /v1/work-orders/:id` — Delete Word Order
- `GET /v1/work-orders/:id` — Get Work Order
- `PATCH /v1/work-orders/:id` — Update Work Order
    - body: parent_work_order_id ((optional, exists:work_orders.id)), service_external_id ((optional, exists:services_external.id)), service_internal_id ((optional, exists:services_internal.id)), upgrade_id ((optional, exists:upgrades.id)), facility_id ((optional, exists:facilities.id)), delivery_note_issued_id ((optional, exists:delivery_notes_issued.id)), order_sale_id ((optional, exists:orders_sale.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional)), date_delivery_expected ((optional)), date_delivery_expected_first ((optional)), date_start_expected ((optional)), date_stop_expected ((optional)), date_diff ((optional)), amount_total ((optional)), priority_order ((optional)), production_planner_bin_id ((optional))
- `POST /v1/work-orders/:id/complete-promo` — Work order complete promo
- `POST /v1/work-orders/:id/detach` — Get Work Order
- `POST /v1/work-orders/:id/detach` — Get Work Order
- `POST /v1/work-orders/:id/detach` — Get Work Order
- `POST /v1/work-orders/:id/rebook` — Work order rebook
    - body: serials ((required if no quantity)), quantity ((required if no serials)), warehouse_location_id ((optional))
- `GET /v1/work-orders/:id/value` — WorkOrderValue
- `POST /v1/work-orders/:id/virtual-reservation` — Virtual reserve work order material
- `GET /v1/work-orders/all` — Get All Work Orders
- `GET /v1/work-orders/all` — Get All Work Orders
- `GET /v1/work-orders/all` — Get All Work Orders
- `GET /v1/work-orders/all` — Get All Work Orders
- `GET /v1/work-orders/all` — Get All Work Orders
- `POST /v1/work-orders/{id}/create-work-orders` — Create work orders for packing
    - body: parent_work_order_id ((optional, exists:work_orders.id)), service_external_id ((optional, exists:services_external.id)), service_internal_id ((optional, exists:services_internal.id)), upgrade_id ((optional, exists:upgrades.id)), facility_id ((optional, exists:facilities.id)), delivery_note_issued_id ((optional, exists:delivery_notes_issued.id)), order_sale_id ((optional, exists:orders_sale.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional)), date_delivery_expected ((optional)), date_delivery_expected_first ((optional)), date_start_expected ((optional)), date_stop_expected ((optional)), date_diff ((optional)), amount_total ((optional)), priority_order ((optional)), production_planner_bin_id ((optional))
- `POST /v1/work-orders/{id}/split-to-single-piece` — Split work order single piece
    - body: parent_work_order_id ((optional, exists:work_orders.id)), service_external_id ((optional, exists:services_external.id)), service_internal_id ((optional, exists:services_internal.id)), upgrade_id ((optional, exists:upgrades.id)), facility_id ((optional, exists:facilities.id)), delivery_note_issued_id ((optional, exists:delivery_notes_issued.id)), order_sale_id ((optional, exists:orders_sale.id)), document_type_id ((required, exists:document_types.id)), document_number ((required, max:255)), reference_number ((optional)), date_delivery_expected ((optional)), date_delivery_expected_first ((optional)), date_start_expected ((optional)), date_stop_expected ((optional)), date_diff ((optional)), amount_total ((optional)), priority_order ((optional)), production_planner_bin_id ((optional))

## Work_Orders_Items
- `POST /v1/work-order-items/:id/transfer-to-location/:userId? Transfer work order material` — to location

## Work_equipment
- `GET /v1/work-equipment` — Lists All Work equipment

## Work_location
- `GET /v1/work-locations` — Lists All Work locations
- `PATCH /v1/work-locations/:id` — Update Work locations
    - body: name ((required)), paid_lunch ((optional)), hidden ((optional))

## Work_locations
- `POST /v1/work-locations` — Create work locations
    - body: name ((required)), paid_lunch ((optional)), hidden ((optional))
- `GET /v1/work-locations/:id` — Get Work locations

## Work_position_Hr_department
- `PATCH /v1/work-position-hr-department/:id` — Update work position hr department
    - body: from ((required)), to ((required)), user_work_position_id ((required, exists:user_work_positions.id)), hr_department_id ((required, exists:hr_departments.id))

## Work_position_hr_department
- `GET /v1/work-position-hr-department` — Lists All work position hr departments
- `POST /v1/work-position-hr-department` — Create work position hr departments
    - body: from ((required)), to ((required)), user_work_position_id ((required, exists:user_work_positions.id)), hr_department_id ((required, exists:hr_departments.id))
- `DELETE /v1/work-position-hr-department/:id` — Delete Work Position Hr department
- `GET /v1/work-position-hr-department/:id` — Get work position hr department
- `GET /v1/work-position-hr-department/all` — Get all work position hr departments

## Workflow
- `GET /v1/user-hr-profiles/entry-registration-types` — Get event types for registration
- `GET /v1/workflow-approval/:id` — Get refresh users attendance
- `POST /v1/workflow-approval/generate-employment-contracts` — Generate employment contracts
- `POST /v1/workflow-approval/generate-vacation-contracts` — Generate vacation contracts
- `POST /v1/workflow-approval/get-active-employees` — Get Active employees
- `POST /v1/workflow-approval/get-employees-events-for-lead` — Get events of given employees for lead
- `POST /v1/workflow-approval/get-employees-fluctuation` — Get employees fluctuation
- `POST /v1/workflow-approval/get-employees-for-coworkers-view` — Get employees for coworkers view
- `GET /v1/workflow-approval/get-events-for-month` — Get Events For Month
- `GET /v1/workflow-approval/get-grouped-events-by-month` — Get Events Grouped By Month
- `GET /v1/workflow-approval/get-lead-for-user` — Get lead For User
- `GET /v1/workflow-approval/get-leave-for-user` — Get Leave For User
- `GET /v1/workflow-approval/get-saldo-for-user` — Get Saldo For User
- `GET /v1/workflow-approval/get-saldos-in-month-for-user` — Get Saldos In Month For User
- `GET /v1/workflow-approval/is-day-event-free` — Get Is Day Event Free
- `GET /v1/workflow-approval/is-day-substitution-valid` — Get Is Day Substitution Valid
- `POST /v1/workflow-approval/new-current-time-registration` — New current time registration
- `POST /v1/workflow-approval/start-process-for-business-trip` — Start process for business trip
- `GET /v1/workflow-approval/todayPresence` — Get Today Presence