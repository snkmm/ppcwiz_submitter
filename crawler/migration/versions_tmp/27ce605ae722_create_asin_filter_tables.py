"""create asin filter tables

Revision ID: 27ce605ae722
Revises: 751f7696f67b
Create Date: 2021-04-08 17:16:49.636516

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '27ce605ae722'
down_revision = '751f7696f67b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sb_filter_acos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile_id', sa.BigInteger(), nullable=False),
    sa.Column('campaign_id', sa.BigInteger(), nullable=False),
    sa.Column('ad_group_id', sa.BigInteger(), nullable=False),
    sa.Column('keyword_text', sa.String(length=80), nullable=False),
    sa.Column('match_type', sa.Enum('NEGATIVE_EXACT', 'NEGATIVE_PHRASE', name='acosmatchtype'), nullable=False),
    sa.Column('active', sa.Boolean(), server_default='1', nullable=False),
    sa.Column('created_datetime', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_datetime', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('saved', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sb_filter_acos_id'), 'sb_filter_acos', ['id'], unique=False)
    op.create_table('sp_filter_acos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile_id', sa.BigInteger(), nullable=False),
    sa.Column('campaign_id', sa.BigInteger(), nullable=False),
    sa.Column('ad_group_id', sa.BigInteger(), nullable=False),
    sa.Column('state', sa.Enum('PAUSED', 'ENABLED', 'ARCHIVED', name='state'), nullable=False),
    sa.Column('keyword_text', sa.String(length=80), nullable=False),
    sa.Column('match_type', sa.Enum('NEGATIVE_EXACT', 'NEGATIVE_PHRASE', name='acosmatchtype'), nullable=False),
    sa.Column('active', sa.Boolean(), server_default='1', nullable=False),
    sa.Column('created_datetime', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_datetime', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('saved', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sp_filter_acos_id'), 'sp_filter_acos', ['id'], unique=False)
    op.alter_column('dtb_profile', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('dtb_profile', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('dtb_user', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('dtb_user', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_ad_group', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_ad_group', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_campaign', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_campaign', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_filter_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_filter_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_keyword_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_keyword_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_ad_group', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_ad_group', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_campaign', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_campaign', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_neg_target', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_neg_target', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_product_ad', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_product_ad', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_target', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_target', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_target_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_target_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_ad_group', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_ad_group', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_camp_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_camp_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_campaign', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_campaign', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_filter_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_filter_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_keyword_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_keyword_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_neg_target', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_neg_target', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_product_ad', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_product_ad', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_product_ad_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_product_ad_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_target', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_target', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_target_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_target_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sp_target_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_target_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_target', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_target', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_product_ad_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_product_ad_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_product_ad', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_product_ad', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_neg_target', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_neg_target', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_keyword_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_keyword_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_filter_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_filter_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_campaign', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_campaign', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_camp_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_camp_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_ad_group', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_ad_group', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_target_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_target_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_target', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_target', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_product_ad', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_product_ad', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_neg_target', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_neg_target', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_campaign', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_campaign', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_ad_group', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_ad_group', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_keyword_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_keyword_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_filter_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_filter_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_campaign', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_campaign', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_ad_group', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_ad_group', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('dtb_user', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('dtb_user', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('dtb_profile', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('dtb_profile', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.create_table('sb_filter_acos',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('profile_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('campaign_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('ad_group_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('keyword_text', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('match_type', mysql.ENUM('NEGATIVE_EXACT', 'NEGATIVE_PHRASE'), nullable=False),
    sa.Column('active', mysql.TINYINT(display_width=1), server_default=sa.text("'1'"), autoincrement=False, nullable=False),
    sa.Column('created_datetime', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_datetime', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('saved', mysql.FLOAT(), nullable=True),
    sa.CheckConstraint('(`active` in (0,1))', name='sb_filter_acos_chk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_sb_filter_acos_id', 'sb_filter_acos', ['id'], unique=False)
    op.create_table('sp_filter_acos',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('profile_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('campaign_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('ad_group_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('state', mysql.ENUM('PAUSED', 'ENABLED', 'ARCHIVED'), nullable=False),
    sa.Column('keyword_text', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('match_type', mysql.ENUM('NEGATIVE_EXACT', 'NEGATIVE_PHRASE'), nullable=False),
    sa.Column('active', mysql.TINYINT(display_width=1), server_default=sa.text("'1'"), autoincrement=False, nullable=False),
    sa.Column('created_datetime', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_datetime', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('saved', mysql.FLOAT(), nullable=True),
    sa.CheckConstraint('(`active` in (0,1))', name='sp_filter_acos_chk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_sp_filter_acos_id', 'sp_filter_acos', ['id'], unique=False)
    # ### end Alembic commands ###
