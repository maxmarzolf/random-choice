"""empty message

Revision ID: 702aa9afe449
Revises: 295d39dccd2d
Create Date: 2020-07-26 21:03:49.120745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '702aa9afe449'
down_revision = '295d39dccd2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('writer')
    op.add_column('user', sa.Column('user_about', sa.String(length=200), nullable=True))
    op.add_column('user', sa.Column('user_subtitle', sa.String(length=40), nullable=True))
    op.add_column('user', sa.Column('user_website', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'user_website')
    op.drop_column('user', 'user_subtitle')
    op.drop_column('user', 'user_about')
    op.create_table('writer',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('writer_user_id', sa.INTEGER(), nullable=False),
    sa.Column('writer_about_me', sa.VARCHAR(length=200), nullable=True),
    sa.Column('writer_short_summary', sa.VARCHAR(length=40), nullable=True),
    sa.ForeignKeyConstraint(['writer_user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
