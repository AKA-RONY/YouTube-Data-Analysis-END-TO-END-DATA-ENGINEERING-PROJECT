
        
import awswrangler as wr
import pandas as pd
import os
import urllib.parse

os_input_s3_cleansed_layer = os.environ['s3_cleansed_layer']
os_input_glue_catalog_db_name = os.environ['glue_catalog_db_name']
os_input_glue_catalog_table_name = os.environ['glue_catalog_table_name']
os_input_write_data_operation = os.environ['write_data_operation']



def lambda_handler(event, context):
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name'] #the bucket and key is fetched from the event i.e when we perform 'configure-test-event' while we 'Test' the function inside s3 template we manually provided the s3 bucket_name as well as the key for individual file location; so when  we run the lambda function it fetch the bucket name as well as the key name from the event. 
    key= urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'],encoding='utf-8')
    
    try:
        
        # creating DF from content
        df_raw= wr.s3.read_json('s3://{}/{}'.format(bucket,key))
        
        #extract required columns:
        df_step_1= pd.json_normalize(df_raw['items'])
        
        
        #write to s3
        wr_response= wr.s3.to_parquet(
            df=df_step_1,
            path=os_input_s3_cleansed_layer,
            dataset=True,
            database=os_input_glue_catalog_db_name,
            table=os_input_glue_catalog_table_name,
            mode=os_input_write_data_operation
            )
            
        return wr_response
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. make sure they exist and your bucket is in the same region as this function '.format(key,bucket))
        raise e        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        