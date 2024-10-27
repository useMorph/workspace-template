{{
    config(
        name="ga_data_extraction",
        description="Extract data for page views including user_pseudo_id, page_location, and event_timestamp from the events_ table. It will include only events with event_name 'page_view'",
        connection="bq_google_analytics",
        schema=[
         {
            "name": "user_pseudo_id",
            "description": "The unique identifier for a user",
            "type": "STRING"
         },
         {
            "name": "page_location",
            "description": "The URL of the visited page",
            "type": "STRING"
         },
         {
            "name": "page_referrer",
            "description": "The URL of the visited page before page_location.",
            "type": "STRING"
         },
         {
            "name": "event_timestamp",
            "description": "The timestamp of the event in microseconds since epoch",
            "type": "INTEGER"
         }
      ]
    )
}}

SELECT user_pseudo_id,
   (
      SELECT
         value.string_value
      FROM
         UNNEST(event_params)
         WHERE
            key = 'page_location'
   ) AS page_location,
   (
      SELECT
         value.string_value
      FROM
         UNNEST(event_params)
         WHERE
            key = 'page_referrer'
   ) AS page_referrer,
      event_timestamp
FROM `[PUT_YOUR_PROJECT_ID].[PUT_YOUR_DATASET: analytics_***].events_*`, UNNEST(event_params)
WHERE
   event_name = 'page_view'