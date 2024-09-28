import { mysqlTable, varchar, char, datetime } from 'drizzle-orm/mysql-core';

export const users = mysqlTable('users', {
  id: char('id', { length: 36 }).primaryKey(),
  email: varchar('email', { length: 150 }).notNull().unique(),
  username: varchar('username', { length: 150 }).notNull().unique(),
  password: varchar('password', { length: 255 }).notNull(),
  firstName: varchar('firstName', { length: 255 }).notNull(),
  lastName: varchar('lastName', { length: 255 }),
  createdAt: datetime('createdAt').notNull(),
  updatedAt: datetime('updatedAt').notNull()
});

// everytime we have changes on schema and it changes directly to the sql
//npx drizzle-kit generate
//npx drizzle-kit push
