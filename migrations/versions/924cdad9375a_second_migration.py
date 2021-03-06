"""Second migration

Revision ID: 924cdad9375a
Revises: 9c7ad1fe9bbd
Create Date: 2018-09-16 09:00:24.162739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '924cdad9375a'
down_revision = '9c7ad1fe9bbd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('blog_post', sa.String(), nullable=True),
    sa.Column('blog_pic', sa.String(), nullable=True),
    sa.Column('photo_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blogs')
    # ### end Alembic commands ###
